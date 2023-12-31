import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

## PARA EJECUTAR EL ARCHIVO REEMPLAZAR RUTA POR data/personas.csv"
PERSONAS_CSV_ROUTE = '../data/personas.csv'

class Personas:

    # Constructo definiendo los atributos
    def __init__(self, nombre, fecha_nacimiento, genero, codigo_postal, id = None) -> None:
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.codigo_postal = codigo_postal
        self.id = id

    # Dunder para imprimir atributos del objeto instanciado
    def __repr__(self) -> str:
        string = list()
        string.append(f'ID: {self.id}')
        string.append(f'Fecha nacimiento: {self.fecha_nacimiento}')
        string.append(f'Genero: {self.genero}')
        string.append(f'Codigo postal: {self.codigo_postal}')
        return "\n".join(string)

    def get_age(self) -> int:
        # Metodo que retorna el año de nacimiento a partir de la fecha de nacimiento
        today = datetime.today()
        year_from_age = today.year - self.fecha_nacimiento.year
        return year_from_age

    #Metodo que retorna un dataframe a partir del archivo csv en la ruta pasada por parametro filename
    @classmethod
    def create_df_from_csv(cls, filename) -> pd.DataFrame:
        df_personas = pd.read_csv(filename)
        return df_personas

    @classmethod
    def get_from_df(cls, df_mov, id=None, nombre=None, anios=None, generos=None) -> pd.DataFrame:
        query = []

        if id is not None:
            query.append(f'id == {id} ')
        if nombre is not None:
            query.append(f' `Full Name` == "{nombre}" ')
        if anios is not None:
            today = datetime.today()
            year_from_age = today.year - anios
            query.append(f' `year of birth` == {year_from_age} ')
        if generos is not None:
            query.append(f'Gender == "{generos}" ')

        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df_mov.query(query_str)
        else:
            result_df = df_mov

        return result_df
    
    @classmethod
    def get_stats(cls, df_personas, anios=None, generos=None) -> None:
        # Utlizo el metodo get_from_df para obtener un dataframe con los registros que coincidan con los parametros pasados
        result_df = cls.get_from_df(df_personas, anios=anios, generos=generos)

        #Cantidad total de tuplas segun query (personas)
        print(f'Cantidad total de personas segun busqueda: {result_df.shape[0]}')
       

        # Crea un histograma para cada género de la cantidad nacida de hombres y mujeres por año
        #  siempre y cuando lo años y generos no se especifiquen
        if anios == None and generos == None:
             # Creacion de dataframe para cada género
            df_hombres = result_df[result_df['Gender'] == 'M']
            df_mujeres = result_df[result_df['Gender'] == 'F']
            plt.hist(df_hombres['year of birth'], bins=range(result_df['year of birth'].min(), result_df['year of birth'].max()+1), alpha=1, label='Hombres', color='blue', edgecolor='black')
            plt.hist(df_mujeres['year of birth'], bins=range(result_df['year of birth'].min(), result_df['year of birth'].max()+1), alpha=1, label='Mujeres', color='pink', edgecolor='black')

            plt.title('Distribución de años de nacimiento por género')
            plt.xlabel('Año de nacimiento')
            plt.ylabel('Cantidad de personas')
            plt.title('Distibución de años de nacimiento por género')
            plt.title(f'Total: {result_df.shape[0]}, Hombres: {df_hombres.shape[0]}, Mujeres: {df_mujeres.shape[0]}')
            # Añade leyenda para indicar qué color corresponde a cada género
            plt.legend(loc='upper right')
            plt.show()



    # Metodo  debe ser sobreescrito en las clases hijas, ya que crearemos un metodo 
    # para cada usuario o trabajadores que hereden de esta clase.
    def write_df(self, df_personas, overwrite=False) -> None:
        
        edad = self.get_age()


        if self.id is not None:
            if overwrite:
                df_personas.loc[df_personas['id'] == self.id] = [self.id, self.nombre, edad, self.genero, self.codigo_postal]
                df_personas.to_csv(PERSONAS_CSV_ROUTE, index=False)
                print("Se ha actualizado el registro personas.")
            else:
                  raise ValueError(f'Habilite la sobreescritura si usted intenta modificar un registro con el ID.')
        else:
            self.id = df_personas['id'].max() + 1
            df_personas.loc[df_personas.shape[0]] = [self.id, self.nombre, edad, self.genero, self.codigo_postal]
            df_personas.to_csv(PERSONAS_CSV_ROUTE, index=False)
            print("Se ha creado el registro en personas.")


    
    # Metodo que elimina un registro de personas en el archivo csv solamente cuando todos los atributos del objeto instanciado 
    # coinciden con los del registro   
    def remove_from_df(self, df_personas) -> None:
        
        edad = self.get_age()
        match = ( 
                  (df_personas['id'] == self.id) &
                  (df_personas['Full Name'] == self.nombre) &
                  (df_personas['year of birth'] == edad) &
                  (df_personas['Gender'] == self.genero) &
                  (df_personas['Zip Code'] == self.codigo_postal)
                )
        
        if match.any():
            df_personas.drop(match[match].index, inplace=True)
            df_personas.reset_index(drop=True, inplace=True)
            df_personas.to_csv(PERSONAS_CSV_ROUTE, index=False)
            print("Se ha eliminado el registro de personas.")
        else:
            print("No se ha encontrado el registro de personas.")
           

    
# Metodo que retorna un dataframe a partir del archivo csv en la ruta pasada por parametro
# df_personas = Personas.create_df_from_csv(PERSONAS_CSV_ROUTE)


# estadisticas, si no pasamos nada, no plotea, si pasamos nos devuelve un print
#Personas.get_stats(df_personas)

# p = Personas(
#     fecha_nacimiento= datetime(1950, 1, 1),
#     nombre = 'Lucas Martinez',
#     genero='M',
#     codigo_postal='24151',
# )
#p.write_df(df_personas)





