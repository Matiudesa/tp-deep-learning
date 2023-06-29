from datetime import datetime
from users import csv_filename
from peliculas import PELICULAS_CSV_ROUTE
import pandas as pd

SCORES_CSV_ROUTE = 'data/scores.csv'

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
    def create_df_from_csv(cls, filename) -> pd.DataFrame:
        df_scores = pd.read_csv(filename)
        df_scores["Date"] = df_scores["Date"].fillna('1900-01-01')
        df_scores["Date"] = df_scores["Date"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        return df_scores

    def write_df(self, df_scores, overwrite=False) -> None:

        df_peliculas = pd.read_csv(PELICULAS_CSV_ROUTE)
        df_usuarios = pd.read_csv(csv_filename)

        if df_usuarios.loc[df_usuarios['id'] == self.usuario_id].empty:
            print("El ID de usuario no existe.")
            return
        # Verificar que el ID de película existe en el DataFrame de películas
        if df_peliculas.loc[df_peliculas['id'] == self.pelicula_id].empty:
            print("El ID de película no existe.")
            return

        # Si los IDs de usuario y película existen, proceder como antes
        if overwrite:
            df_scores.loc[(df_scores['user_id'] == self.usuario_id) & (df_scores['movie_id'] == self.pelicula_id)] = [self.usuario_id, self.pelicula_id, self.puntuacion, self.timestamp]
            df_scores.to_csv(SCORES_CSV_ROUTE, index=False)
        else:
            df_scores.loc[df_scores.shape[0]] = [self.usuario_id, self.pelicula_id, self.puntuacion, self.timestamp]
            df_scores.to_csv(SCORES_CSV_ROUTE, index=False)
            print("Se ha creado el registro en trabajadores.")

    def remove_from_df(self, df_scores) -> None:
        df_scores = df_scores.drop(df_scores[(df_scores['user_id'] == self.usuario_id) & (df_scores['movie_id'] == self.pelicula_id)].index)
        df_scores.to_csv(SCORES_CSV_ROUTE, index=False)

    def get_user_avg(self, df_scores):
        return df_scores.groupby('user_id')['rating'].mean()

    def get_movie_avg(self, df_scores):
        return df_scores.groupby('movie_id')['rating'].mean()

    def get_user_avg_by_id(self, df_scores, user_id):
        user_ratings = df_scores[df_scores['user_id'] == user_id]['rating']
        return user_ratings.mean()

    def get_movie_avg_by_id(self, df_scores, movie_id):
        movie_ratings = df_scores[df_scores['movie_id'] == movie_id]['rating']
        return movie_ratings.mean()


df_scores = Scores.create_df_from_csv(SCORES_CSV_ROUTE)

score = Scores(
    usuario_id=1,
    pelicula_id=1,
    puntuacion=5,
    timestamp=datetime.now()
)

'''
user_avg = score.get_user_avg(df_scores)
print("Calificación promedio por usuario:")
print(user_avg)

movie_avg = score.get_movie_avg(df_scores)
print("Calificación promedio por película:")
print(movie_avg)
'''
id = 5
movie_avg_by_id = score.get_movie_avg_by_id(df_scores, id)
print(f"Calificación promedio de la película con ID {id}:")
print(movie_avg_by_id)





