from peliculas import PELICULAS_CSV_ROUTE
from personas import PERSONAS_CSV_ROUTE
from scores import SCORES_CSV_ROUTE
from trabajadores import TRABAJADORES_CSV_ROUTE
import shutil

def save_all(df_personas, df_trabajadores, df_usuarios, df_peliculas, df_scores, file_personas="personas.csv", file_trabajadores="trabajadores.csv", file_usuarios="users.csv", file_peliculas="peliculas.csv", file_scores="scores.csv"):

    route = "../data/"
    try:
        df_personas.to_csv(route + file_personas, index=False)
        df_trabajadores.to_csv(route + file_trabajadores, index=False)
        df_usuarios.to_csv(route + file_usuarios, index=False)
        df_peliculas.to_csv(route + file_peliculas, index=False)
        df_scores.to_csv(route + file_scores, index=False)
        return 0
    except Exception as e:
        return -1




def save_backup():
    shutil.copyfile(PELICULAS_CSV_ROUTE, 'backup/peliculas.csv')
    shutil.copyfile(PERSONAS_CSV_ROUTE, 'backup/personas.csv')
    shutil.copyfile(SCORES_CSV_ROUTE, 'backup/scores.csv')
    shutil.copyfile(TRABAJADORES_CSV_ROUTE, 'backup/trabajadores.csv')
    print("Se han guardado todos los archivos CSV.")
