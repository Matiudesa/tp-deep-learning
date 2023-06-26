import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

PELICULAS_CSV_ROUTE = 'data/peliculas.csv'

class Pelicula:
    def __init__(self, nombre, fecha_estreno, generos, id = None):
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
        self.generos = generos
        self.id = id
    def __repr__(self):
        strings = list()
        strings.append(f'Nombre: {self.nombre}')
        strings.append(f'Fecha de estreno: {self.fecha_estreno}')
        strings.append(f'Géneros: {self.generos}')
        strings.append(f'ID: {self.id}')
        return "\n".join(strings)
        # Este método debe imprimir la información de esta película.
    def write_df(self, df_mov, overwrite = False):
        pass
        # Este método recibe el dataframe de películas y agrega la película
        # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
        # id ya existe, no la agrega y devuelve un error, salvo que overwrite esté 
        # en True, en cuyo caso, sobreescribe.
    @classmethod
    def create_df_from_csv(cls, filename):
        df_mov = pd.read_csv(filename)
        df_mov["Release Date"] = df_mov["Release Date"].fillna('1-Jan-1900')
        df_mov["Release Date"] = df_mov["Release Date"].apply(lambda x: datetime.strptime(x, '%d-%b-%Y'))
        return df_mov

    @classmethod    
    def get_from_df(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
        query = []

        if (id is not None):
                query.append(f' `id` == "{id}" ')
        if (nombre is not None):
                query.append(f' `Name` == "{nombre}" ')
        if (anios is not None):
                today = datetime.today()
                year_from_date = today.year - anios
                query.append(f' `Release Date` == {year_from_date} ')
        if (generos is not None):
            for genero in generos:
                query.append(f'`{genero}` == 1')

        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df_mov.query(query_str)
        else:
            result_df = df_mov
       
        return result_df

    @classmethod
    def get_stats(cls,df_mov, anios=None, generos=None):
        pass
        # Este class method imprime una serie de estadísticas calculadas sobre
        # los resultados de una consulta al DataFrame df_mov. 
        # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
        # anios: [desde_año, hasta_año]
        # generos: [generos]
        # Las estadísticas son:
        # - Datos película más vieja
        # - Datos película más nueva
        # - Bar plots con la cantidad de películas por año/género.
    def remove_from_df(self, df_mov):
        pass
        # Borra del DataFrame el objeto contenido en esta clase.
        # Para realizar el borrado todas las propiedades del objeto deben coincidir
        # con la entrada en el DF. Caso contrario imprime un error.

#Dataframe
df_mov = Pelicula.create_df_from_csv(PELICULAS_CSV_ROUTE)

print(Pelicula.get_from_df(df_mov,generos=['Action', 'Thriller']), )
