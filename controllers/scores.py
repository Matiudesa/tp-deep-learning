from datetime import datetime
from users import USERS_CSV_ROUTE
from peliculas import PELICULAS_CSV_ROUTE
from personas import PERSONAS_CSV_ROUTE
import pandas as pd
import matplotlib.pyplot as plt

## PARA EJECUTAR EL ARCHIVO REEMPLAZAR RUTA POR data/scores.csv"
SCORES_CSV_ROUTE = '../data/scores.csv'

class Scores:

    def __init__(self, usuario_id, pelicula_id, puntuacion, timestamp) -> None:
        self.usuario_id = usuario_id
        self.pelicula_id = pelicula_id
        self.puntuacion = puntuacion
        self.timestamp = timestamp

    def __repr__(self) -> str:
        string = list()
        string.append(f'Usuario ID: {self.usuario_id}')
        string.append(f'Pelicula ID: {self.pelicula_id}')
        string.append(f'Puntuacion: {self.puntuacion}')
        string.append(f'Timestamp: {self.timestamp}')
        return "\n".join(string)

    @classmethod
    def create_df_from_csv(cls, filename: str) -> pd.DataFrame:
        df_scores = pd.read_csv(filename)
        df_scores["Date"] = df_scores["Date"].fillna('1900-01-01')
        df_scores["Date"] = df_scores["Date"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        return df_scores
    
    @classmethod
    def get_from_df(cls, df_scores, usuario_id=None, pelicula_id=None, puntuacion=None) -> pd.DataFrame:
        query = []

        if usuario_id is not None:
            query.append(f' user_id == {usuario_id} ')
        if pelicula_id is not None:
            query.append(f'movie_id == {pelicula_id}')
        if puntuacion is not None:
            query.append(f' rating == {puntuacion}')

        if len(query) > 0:
            query_str = " and ".join(query)
            result_df = df_scores.query(query_str)
        else:
            result_df = df_scores

        return result_df
    def write_df(self, df_scores, overwrite=False) -> None:

        df_peliculas = pd.read_csv(PELICULAS_CSV_ROUTE)
        df_usuarios = pd.read_csv(USERS_CSV_ROUTE)

        if df_usuarios.loc[df_usuarios['id'] == self.usuario_id].empty:
            print("El ID de usuario no existe.")
            return
        # Verificar que el ID de película existe en el DataFrame de películas
        if df_peliculas.loc[df_peliculas['id'] == self.pelicula_id].empty:
            print("El ID de película no existe.")
            return
        
        # el Timestamp no debe tener milisegundos

        self.timestamp = self.timestamp.replace(microsecond=0)


        # Si los IDs de usuario y película existen, proceder como antes
        if overwrite:
            row_index = df_scores.loc[(df_scores['user_id'] == self.usuario_id) & (df_scores['movie_id'] == self.pelicula_id)].index[0]
            df_scores.loc[(df_scores['user_id'] == self.usuario_id) & (df_scores['movie_id'] == self.pelicula_id)] = [row_index, self.usuario_id, self.pelicula_id, self.puntuacion, self.timestamp]
            df_scores.to_csv(SCORES_CSV_ROUTE, index=False)
            print(f'Se ha actualizado la puntuacion de la pelicula {df_peliculas.loc[df_peliculas["id"] == self.pelicula_id]["Name"].values[0]}')
        else:
            df_scores.loc[df_scores.shape[0]] = [df_scores.shape[0], self.usuario_id, self.pelicula_id, self.puntuacion, self.timestamp]
            df_scores.to_csv(SCORES_CSV_ROUTE, index=False)
            print(f'{self.puntuacion} puntos para la película {df_peliculas.loc[df_peliculas["id"] == self.pelicula_id]["Name"].values[0]}')
    
    def remove_from_df(self, df_scores) -> None:

        # matcheamos todas las propiedades del objeto
        # No tiene sentido pasar un timestamp ya que toma el horario actual, eliminaremos solo por usuario y película y puntuacion
        match = (
                (df_scores['user_id'] == self.usuario_id) & 
                (df_scores['movie_id'] == self.pelicula_id) &
                (df_scores['rating'] == self.puntuacion)
        )
        
        if match.any():
            row_index = df_scores.loc[match].index[0]
            df_scores = df_scores.drop(row_index)
            df_scores.to_csv(SCORES_CSV_ROUTE, index=False)
            print(f'Se ha eliminado la puntuacion de la pelicula {self.pelicula_id}')
        else:
            print(f'No se ha encontrado puntuacion a eliminar')

        # df_scores = df_scores.drop(df_scores[(df_scores['user_id'] == self.usuario_id) & (df_scores['movie_id'] == self.pelicula_id)].index)
        # df_scores.to_csv(SCORES_CSV_ROUTE, index=False)
    @staticmethod
    def get_user_avg(df_scores) -> pd.DataFrame:
        return df_scores.groupby('user_id')['rating'].mean()

    @staticmethod
    def get_movie_avg(df_scores) -> pd.DataFrame:
        return df_scores.groupby('movie_id')['rating'].mean()


    @staticmethod
    def get_user_avg_by_id(df_scores, user_id) -> pd.DataFrame:
        user_ratings = df_scores[df_scores['user_id'] == user_id]['rating']
        return user_ratings.mean()

    @staticmethod
    def get_movie_avg_by_id(df_scores, movie_id) -> int:
        movie_ratings = df_scores[df_scores['movie_id'] == movie_id]['rating']
        return int(movie_ratings.mean())    

# df_scores = Scores.create_df_from_csv(SCORES_CSV_ROUTE)

# score = Scores(
#     usuario_id=12,
#     pelicula_id=203,
#     puntuacion=1,
#     timestamp=datetime.now()
#     )

# Scores.get_stats(df_scores)

#score.write_df(df_scores, overwrite=True)
#score.remove_from_df(df_scores)
'''
user_avg = score.get_user_avg(df_scores)
print("Calificación promedio por usuario:")
print(user_avg)

movie_avg = score.get_movie_avg(df_scores)
print("Calificación promedio por película:")
print(movie_avg)
'''
# id = 5
# movie_avg_by_id = score.get_movie_avg_by_id(df_scores, id)
# print(f"Calificación promedio de la película con ID {id}:")
# print(movie_avg_by_id)


# Obtener del dataframe
# print(Scores.get_from_df(df_scores, usuario_id=2))

# Eliminar mediante matcheos
# score.remove_from_df(df_scores)



