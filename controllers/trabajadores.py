from personas import Personas, PERSONAS_CSV_ROUTE
import pandas as pd

TRABAJADORES_CSV_ROUTE = 'data/trabajadores.csv'

class Trabajadores(Personas):

    def __init__(self, nombre, fecha_nacimiento, genero, codigo_postal, fecha_alta, puesto, horario_trabajo, categoria, id = None):
        super().__init__(nombre, fecha_nacimiento, genero, codigo_postal, id)
        self.fecha_alta = fecha_alta
        self.puesto = puesto
        self.horario_trabajo = horario_trabajo
        self.categoria = categoria
        
    def __repr__(self):
        base_repr = super().__repr__()
        trabajadores_repr = list()
        trabajadores_repr.append(f'Fecha_alta: {self.fecha_alta}')
        trabajadores_repr.append(f'Puesto: {self.puesto}')
        trabajadores_repr.append(f'Horario de trabajo: {self.horario_trabajo}')
        trabajadores_repr.append(f'Categoria: {self.categoria}')
        return base_repr + "\n" + "\n".join(trabajadores_repr)
    
    @classmethod
    def create_df_from_csv(cls, filename):
        df_trabajadores = pd.read_csv(filename)
        return df_trabajadores


    def write_df(self, df_trabajadores, overwrite = False):  
        
        if self.id is not None:
            if overwrite:
                df_trabajadores.loc[df_trabajadores['id'] == self.id] = [ self.id, self.puesto, self.categoria, self.horario_trabajo, self.fecha_alta]
                df_trabajadores.to_csv(TRABAJADORES_CSV_ROUTE, index=False)
                print("Se ha actualizado el registro en trabajadores.")
            else:
                 raise ValueError(f'El ID {self.id} ya existe en el archivo.')
        else:
            df_personas = super().create_df_from_csv(PERSONAS_CSV_ROUTE)    
            super().write_df(df_personas)
            self.id = df_personas.shape[0]
            df_trabajadores.loc[df_trabajadores.shape[0]] = [self.id, self.puesto, self.categoria, self.horario_trabajo, self.fecha_alta]
            df_trabajadores.to_csv(TRABAJADORES_CSV_ROUTE, index=False)
            print("Se ha creado el registro en trabajadores.")
            


# Objeto instanciado para probar el funcionamiento de la clase
t = Trabajadores(
    fecha_alta= '15/05/2005',
    fecha_nacimiento= '2000',
    nombre = 'Lucas Martinez',
    genero='M',
    categoria='A',
    puesto='IT',
    horario_trabajo='9-18',
    codigo_postal='B1713'
)

# Metodo que retorna un dataframe a partir del archivo csv en la ruta pasada por parametro
df_trabajadores = Trabajadores.create_df_from_csv(TRABAJADORES_CSV_ROUTE)
