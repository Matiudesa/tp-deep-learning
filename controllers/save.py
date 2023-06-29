from peliculas import PELICULAS_CSV_ROUTE
from personas import PERSONAS_CSV_ROUTE
from scores import SCORES_CSV_ROUTE
from trabajadores import TRABAJADORES_CSV_ROUTE
import shutil

def save_all():
    shutil.copyfile(PELICULAS_CSV_ROUTE, 'backup/peliculas.csv')
    shutil.copyfile(PERSONAS_CSV_ROUTE, 'backup/personas.csv')
    shutil.copyfile(SCORES_CSV_ROUTE, 'backup/scores.csv')
    shutil.copyfile(TRABAJADORES_CSV_ROUTE, 'backup/trabajadores.csv')
    print("Se han guardado todos los archivos CSV.")


# save_all()
