from personas import Personas, PERSONAS_CSV_ROUTE
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

## PARA EJECUTAR EL ARCHIVO REEMPLAZAR RUTA POR data/trabajadores.csv"
TRABAJADORES_CSV_ROUTE = '../data/trabajadores.csv'

class Trabajadores(Personas):

    def __init__(self, nombre, fecha_nacimiento, genero, codigo_postal, fecha_alta, puesto, horario_trabajo, categoria, id = None) -> None:
        super().__init__(nombre, fecha_nacimiento, genero, codigo_postal, id)
        self.fecha_alta = fecha_alta
        self.puesto = puesto
        self.horario_trabajo = horario_trabajo
        self.categoria = categoria
        
    def __repr__(self) -> str:
        base_repr = super().__repr__()
        trabajadores_repr = list()
        trabajadores_repr.append(f'Fecha_alta: {self.fecha_alta}')
        trabajadores_repr.append(f'Puesto: {self.puesto}')
        trabajadores_repr.append(f'Horario de trabajo: {self.horario_trabajo}')
        trabajadores_repr.append(f'Categoria: {self.categoria}')
        return base_repr + "\n" + "\n".join(trabajadores_repr)
    
    @classmethod
    def create_df_from_csv(cls, filename) -> pd.DataFrame:
        df_trabajadores = pd.read_csv(filename)
        df_trabajadores["Start Date"] = df_trabajadores["Start Date"].fillna('1-Jan-1900')
        df_trabajadores["Start Date"] = df_trabajadores["Start Date"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
        return df_trabajadores
    
    @classmethod
    def get_from_df(cls, df_trabajadores , fechas = None, puesto=None, horario_trabajo=None, categoria=None) -> pd.DataFrame:
        query = []

        if (puesto is not None):
            query.append(f' Position == "{puesto}" ')
        if (categoria is not None):
            query.append(f' Category == "{categoria}" ')
        if (horario_trabajo is not None):
            query.append(f' `Working Hours` == "{horario_trabajo}" ')
        if (fechas is not None):
            assert len(fechas) == 2, 'Debe ingresar una lista de dos fechas'
            desde = fechas[0]
            hasta = fechas[1]
            if hasta == desde:
                hasta = datetime(fechas[1],12,31)
            query.append(f' `Start Date` >= "{desde}" and `Start Date` <= "{hasta}" ')
        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df_trabajadores.query(query_str)
        else:
            result_df = df_trabajadores

        return result_df
    
    @classmethod
    def get_stats(cls, df_trabajadores, puesto = None) -> None:

        if(puesto is not None):
            result_df = df_trabajadores[df_trabajadores['Position'] == puesto]
            print(f'Cantidad de trabajadores en el puesto {puesto}: {result_df.shape[0]}')
        else:
            result_df = df_trabajadores
            print(f'Cantidad de trabajadores: {result_df.shape[0]}')

        cant_por_puesto = result_df['Position'].value_counts()
        plt.figure(figsize=(10,6))
        plt.pie(cant_por_puesto.values, labels=cant_por_puesto.index, autopct='%1.1f%%')
        plt.title('Cantidad de trabajadores por puesto')
        plt.show()

    def write_df(self, df_trabajadores, overwrite = False) -> None:  
        
        if self.id is not None:

        # Cargamos el dataframe de personas y verificamos si el id existe en el dataframe de personas
            df_personas = pd.read_csv(PERSONAS_CSV_ROUTE)
            if df_personas[df_personas['id'] == self.id].empty:
                raise ValueError(f'El ID {self.id} no existe en el archivo de personas.')
            

            if overwrite:
                # Antes de intentar sobrescribir un registro, verificamos que el id exista ya en el dataframe de trabajadores
                if not df_trabajadores[df_trabajadores['id'] == self.id].empty:
                    df_trabajadores.loc[df_trabajadores['id'] == self.id] = [self.id, self.puesto, self.categoria, self.horario_trabajo, self.fecha_alta]
                    df_trabajadores.to_csv(TRABAJADORES_CSV_ROUTE, index=False)
                    print("Se ha actualizado el registro en trabajadores.")
                else:
                    raise ValueError(f'El ID {self.id} no existe en el archivo de trabajadores.')
            else:
                # Antes de intentar crear un nuevo trabajador, verificamos que el id no exista ya en el dataframe de trabajadores
                if df_trabajadores[df_trabajadores['id'] == self.id].empty:
                    df_trabajadores.loc[df_trabajadores.shape[0]] = [self.id, self.puesto, self.categoria, self.horario_trabajo, self.fecha_alta]
                    df_trabajadores.to_csv(TRABAJADORES_CSV_ROUTE, index=False)
                    print("Se ha creado el registro en trabajadores.")
                else:
                    raise ValueError(f'El ID {self.id} ya existe en el archivo de trabajadores.')
        else:
            raise ValueError('No se puede crear un trabajador sin contar con el ID de persona.')
            


    # Buscamos que matcheen todos los campos del trabajador con el registro a eliminar
    def remove_from_df(self, df_trabajadores) -> None:
        match = ( 
              (df_trabajadores['id'] == self.id) &
              (df_trabajadores['Position'] == self.puesto) &
              (df_trabajadores['Category'] == self.categoria) &
              (df_trabajadores['Working Hours'] == self.horario_trabajo) &
              (df_trabajadores['Start Date'] == self.fecha_alta)
            )
        if match.any():
            df_trabajadores.drop(match[match].index, inplace=True)
            df_trabajadores.to_csv(TRABAJADORES_CSV_ROUTE, index=False)
            print("Se ha eliminado el registro del trabajador.")
        else:
            print("No se ha encontrado el registro.")

# Objeto instanciado para probar el funcionamiento de la clase
t = Trabajadores(
    fecha_alta= datetime(1995, 1, 1),
    fecha_nacimiento= '2000',
    nombre = 'Lucas Martinez',
    genero='H',
    categoria='A',
    puesto='IT',
    horario_trabajo='9-18',
    codigo_postal='B1713',
    id=944
)

# Metodo que retorna un dataframe a partir del archivo csv en la ruta pasada por parametro
df_trabajadores = Trabajadores.create_df_from_csv(TRABAJADORES_CSV_ROUTE)
#print(Trabajadores.get_from_df(df_trabajadores, puesto='IT'))
# Estadisticas de los trabajadores
#Trabajadores.get_stats(df_trabajadores, puesto='IT')

# Return del metodo __repr__
# print(t)

#print(Trabajadores.get_from_df(df_trabajadores, categoria='C'))
#t.write_df(df_trabajadores)
