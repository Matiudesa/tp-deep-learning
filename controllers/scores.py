from datetime import datetime
from users import csv_filename
from peliculas import PELICULAS_CSV_ROUTE

SCORES_CSV_ROUTE = 'data/scores.csv'

class Scores():

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
    
    def write_df(self, df_scores, overwrite=False) -> None:

        df_peliculas = pd.read_csv(PELICULAS_CSV_ROUTE)
        df_usuarios = pd.read_csv(USUARIOS_CSV_ROUTE)

        if df_usuarios[df_usuarios['id'] == self.usuario_id].empty:
            print("El ID de usuario no existe.")
            return
        # Verificar que el ID de película existe en el DataFrame de películas
        if df_peliculas[df_peliculas['id'] == self.pelicula_id].empty:
            print("El ID de película no existe.")
            return

        # Si los IDs de usuario y película existen, proceder como antes
        if overwrite:
            df_scores.loc[(df_scores['usuario_id'] == self.usuario_id) & (df_scores['pelicula_id'] == self.pelicula_id)] = [self.usuario_id, self.pelicula_id, self.puntuacion, self.timestamp]
            df_scores.to_csv(SCORES_CSV_ROUTE, index=False)
        else:
            df_scores = df_scores.append({'usuario_id': self.usuario_id, 'pelicula_id': self.pelicula_id, 'puntuacion': self.puntuacion, 'timestamp': self.timestamp}, ignore_index=True)
            df_scores.to_csv(SCORES_CSV_ROUTE, index=False)

        

    
        