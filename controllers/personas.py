from abc import ABC
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

PERSONAS_CSV_ROUTE = 'data/personas.csv'

class Personas():

    # Constructo definiendo los atributos
    def __init__(self, nombre, fecha_nacimiento, genero, codigo_postal, id = None):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.codigo_postal = codigo_postal
        self.id = id


    # Dunder para imprimir atributos del objeto instanciado
    def __repr__(self):
        string = list()
        string.append(f'ID: {self.id}')
        string.append(f'Fecha nacimiento: {self.fecha_nacimiento}')
        string.append(f'Genero: {self.genero}')
        string.append(f'Codigo postal: {self.codigo_postal}')
        return "\n".join(string)

    #Metodo que retorna un dataframe a partir del archivo csv en la ruta pasada por parametro filename
    @classmethod
    def create_df_from_csv(cls, filename):
        df_personas = pd.read_csv(filename)
        return df_personas

    @classmethod
    def get_from_df(cls, df_mov, id=None, nombre=None, anios=None, generos=None):
        query = []

        if (id != None):
            query.append(f'id == {id} ')
        if (nombre != None):
            query.append(f' `Full Name` == "{nombre}" ')
        if (anios != None):
            today = datetime.today()
            year_from_age = today.year - anios
            query.append(f' `year of birth` == {year_from_age} ')
        if (generos != None):
            query.append(f'Gender == "{generos}" ')

        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df_mov.query(query_str)
        else:
            result_df = df_mov

        return result_df


    # Metodo  debe ser sobreescrito en las clases hijas, ya que crearemos un metodo 
    # para cada usuario o trabajadores que hereden de esta clase.
    def write_df(self, df_personas, overwrite=False):
        
        if (self.id != None):
            if overwrite:
                df_personas.loc[df_personas['id'] == self.id] = [self.id, self.nombre, self.fecha_nacimiento, self.genero, self.codigo_postal]
                df_personas.to_csv(PERSONAS_CSV_ROUTE, index=False)
                print("Se ha actualizado el registro personas.")
            else:
                  raise ValueError(f'El ID {self.id} ya existe en el archivo.')
        else:
            self.id = df_personas['id'].max() + 1
            df_personas.loc[df_personas.shape[0]] = [self.id, self.nombre, self.fecha_nacimiento, self.genero, self.codigo_postal]
            df_personas.to_csv(PERSONAS_CSV_ROUTE, index=False)
            print("Se ha creado el registro en personas.")


    @classmethod
    def get_stats(cls, df_personas, anios=None, generos=None):
        query = []

        if(anios != None):
            today = datetime.today()
            year_from_age = today.year - anios
            query.append(f' `year of birth` == {year_from_age} ')
        if(generos != None):
            query.append(f'Gender == "{generos}" ')
        
        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df_personas.query(query_str)
        else:
            result_df = df_personas

        if result_df.empty:
            print("No se encontraron usuarios que cumplan los requisitos.")
            return

        #Cantidad total de tuplas segun query (personas)
        print(f'Cantidad total de personas segun busqueda: {result_df.shape[0]}')
       

        # Crea un histograma para cada género de la cantidad nacida de hombres y mujeres por año
        #  siempre y cuando lo años y generos no se especifiquen
        if anios == None and generos == None:
             # Creacion de dataframe para cada género
            df_hombres = result_df[result_df['Gender'] == 'M']
            df_mujeres = result_df[result_df['Gender'] == 'F']
            plt.hist(df_hombres['year of birth'], bins=range(result_df['year of birth'].min(), result_df['year of birth'].max()+1), alpha=0.5, label='Hombres', color='blue', edgecolor='black')
            plt.hist(df_mujeres['year of birth'], bins=range(result_df['year of birth'].min(), result_df['year of birth'].max()+1), alpha=0.5, label='Mujeres', color='pink', edgecolor='black')

            plt.title('Distribución de años de nacimiento por género')
            plt.xlabel('Año de nacimiento')
            plt.ylabel('Cantidad de personas')
            plt.title('Distibución de años de nacimiento por género')
            plt.title(f'''Distibución de años de nacimiento por género
                      Total: {result_df.shape[0]}, Hombres: {df_hombres.shape[0]}, Mujeres: {df_mujeres.shape[0]}''')
            # Añade leyenda para indicar qué color corresponde a cada género
            plt.legend(loc='upper right')
            plt.show()

    # Metodo que elimina un registro de personas en el archivo csv solamente cuando todos los atributos del objeto instanciado 
    # coinciden con los del registro   
    def remove_from_df(self, df_personas):
       
        match = ( 
                  (df_personas['id'] == self.id) &
                  (df_personas['Full Name'] == self.nombre) &
                  (df_personas['year of birth'] == self.fecha_nacimiento) &
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
df_personas = Personas.create_df_from_csv(PERSONAS_CSV_ROUTE)

p = Personas(
    fecha_nacimiento= 2000,
    nombre = 'Lucas Martinez',
    genero='M',
    codigo_postal='B1713',
)





