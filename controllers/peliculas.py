import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

## PARA EJECUTAR EL ARCHIVO REEMPLAZAR RUTA POR data/peliculas.csv"
PELICULAS_CSV_ROUTE = "../data/peliculas.csv"

class Pelicula:

    def __init__(self, nombre, fecha_estreno, generos, IMDB_URL = None, id = None):
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
        self.IMDB_URL = IMDB_URL
        self.generos = generos
        self.id = id

    def __repr__(self):
        strings = list()
        strings.append(f'Nombre: {self.nombre}')
        strings.append(f'Fecha de estreno: {self.fecha_estreno}')
        strings.append(f'Géneros: {self.generos}')
        strings.append(f'IMDB URL: {self.IMDB_URL}')
        strings.append(f'ID: {self.id}')
        return "\n".join(strings)

    @classmethod
    def create_df_from_csv(cls, filename):
        df_peliculas = pd.read_csv(filename)
        df_peliculas["Release Date"] = df_peliculas["Release Date"].fillna('01-Jan-1900')
        df_peliculas["Release Date"] = df_peliculas["Release Date"].apply(lambda x: datetime.strptime(x, '%d-%b-%Y'))
        return df_peliculas

    @classmethod    
    def get_from_df(cls, df_peliculas, id=None, nombre = None, anios = None, generos = None) -> pd.DataFrame:
        query = []

        if id is not None:
            query.append(f' id == {id} ')
        if nombre is not None:
            query.append(f' Name == "{nombre}" ')
        if anios is not None:
            assert len(anios) == 2, 'El rango de años debe tener dos elementos'
            desde = datetime(anios[0],1,1)
            hasta = datetime(anios[1],1,1)
            if hasta == desde:
                hasta = datetime(anios[1],12,31)
            query.append(f' `Release Date` >= "{desde}" and `Release Date` <= "{hasta}" ')
        if generos is not None:
            for genero in generos:
                query.append(f' {genero} == 1 ')   

        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df_peliculas.query(query_str)
        else:
            result_df = df_peliculas
        
        return result_df
    
    @classmethod
    def get_stats(cls, df_peliculas, anios=None, generos=None) -> None:
        result_from_get = cls.get_from_df(df_peliculas, anios=anios, generos=generos)
        
        if len(result_from_get) > 0:
              # Estadísticas
            print("Película más vieja:")
            pelicula_vieja = df_peliculas[df_peliculas['Release Date'] == df_peliculas['Release Date'].min()]
            print(pelicula_vieja)

            print("\nPelícula más nueva:")
            pelicula_nueva = df_peliculas[df_peliculas['Release Date'] == df_peliculas['Release Date'].max()]
            print(pelicula_nueva)

            # Graficas
            df_peliculas['Release Date'] = df_peliculas['Release Date'].dt.year

            plt.figure(figsize=(16,6))
            plt.subplot(121)
            df_peliculas['Release Date'].value_counts().sort_index().plot(kind='line', marker='o')
            plt.xticks(rotation=45)
            plt.title('Películas por año')
            plt.xlabel('Año')
            plt.ylabel('Cantidad de películas')

            plt.subplot(122)
            df_peliculas[generos].sum().plot(kind='bar')
            plt.title('Películas por género')
            plt.xlabel('Género')
            plt.ylabel('Cantidad de películas')

            plt.tight_layout()
            plt.show()

    
    def write_df(self, df_peliculas, overwrite=False) -> None:
        releaseDate = datetime.strptime(self.fecha_estreno, '%d-%b-%Y')
        formattedDate = releaseDate.strftime('%d-%b-%Y')
        if self.id:
            if self.id in df_peliculas['id'].values:
                if overwrite:
                    row_index = df_peliculas[df_peliculas['id'] == self.id].index[0]
                    df_peliculas.at[row_index, 'Name'] = self.nombre
                    df_peliculas.at[row_index, 'Release Date'] = formattedDate
                    df_peliculas.at[row_index, 'IMDB URL'] = self.IMDB_URL
                    for column in df_peliculas.columns[4:]:
                        df_peliculas.at[row_index, column] = 1 if column in self.generos else 0
                    df_peliculas['Release Date'] = df_peliculas['Release Date'].dt.strftime('%d-%b-%Y')
                    df_peliculas.to_csv(PELICULAS_CSV_ROUTE, index=False)
                    print('Se ha actualizado el DataFrame en el archivo CSV')
                    return df_peliculas
                else:
                    raise ValueError(f'La id {self.id} existe en el DataFrame y pero la sobreescritura esta desactivada')
            else:
                raise ValueError(f'La id {self.id} no se encuentra en el DataFrame.')
        else:
            new_id = df_peliculas['id'].max() + 1
            new_row = pd.DataFrame([{'id': new_id, 'Name': self.nombre, 'Release Date': formattedDate, 'IMDB URL': self.IMDB_URL}])
            for column in df_peliculas.columns[4:]:
                new_row[column] = 1 if column in self.generos else 0
            new_row.to_csv(PELICULAS_CSV_ROUTE, mode='a', index=False, header=False)
            print('Se ha escrito el DataFrame en el archivo CSV')
            return df_peliculas
        

    def remove_from_df(self, df_peliculas) -> None:

        # Crear una serie booleana que indique dónde todas las propiedades del objeto coinciden con las del DataFrame
        match = (
                (df_peliculas['id'] == self.id) & 
                (df_peliculas['Name'] == self.nombre) &                         
                (df_peliculas['Release Date'] == self.fecha_estreno ) &   
                ( (df_peliculas['IMDB URL'] == self.IMDB_URL) | (df_peliculas['IMDB URL'].isna() & pd.isnull(self.IMDB_URL)) )
                )
        for genero in df_peliculas.columns[4:]:
            if genero in self.generos:
                match = match & (df_peliculas[genero] == 1)
            else:
                match = match & (df_peliculas[genero] == 0)
        
        if match.any():
            row_index = df_peliculas[match].index[0]
            df_peliculas.drop(row_index, inplace=True)
            df_peliculas.to_csv(PELICULAS_CSV_ROUTE, index=False)
            df_peliculas['Release Date'] = df_peliculas['Release Date'].dt.strftime('%d-%b-%Y')
            print('Se ha eliminado el registro del DataFrame')
        else:
            raise ValueError('No se ha encontrado el registro en el DataFrame')
        
      
           
# #Dataframe
df_peliculas = Pelicula.create_df_from_csv(PELICULAS_CSV_ROUTE)

# Pelicula.get_stats(df_peliculas, anios=[1994, 1995], generos=['Action'])

# Crear una instancia de la clase Pelicula
# p = Pelicula( 
#     nombre='Avatar2', 
#     fecha_estreno='10-Jan-2202', 
#     generos=['Sci-Fi', 'Action', 'Adventure', 'Fantasy'],
#     id=1683
#   )
# p.remove_from_df(df_peliculas)

    





