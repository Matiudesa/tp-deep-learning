import pandas as pd
from peliculas import PELICULAS_CSV_ROUTE
from personas import PERSONAS_CSV_ROUTE
from trabajadores import TRABAJADORES_CSV_ROUTE
from users import USERS_CSV_ROUTE
from scores import SCORES_CSV_ROUTE
import time


# Funcion para chequear consistencia de dataframes
# Se crea una lista booleana que invierte los valores true y false y solo obtiene los inconsistentes
def consistency_check(df_base, df_check, column, file, check_name):
    boolean_consistency_list = df_check[column].isin(df_base['id'])
    to_delete = boolean_consistency_list[~boolean_consistency_list].index
    df_check.drop(to_delete, inplace=True)
    df_check.to_csv(file, index=False)
    print(f'Dataframe {check_name} checked')
    time.sleep(1)


# Funcion para cargar todos los archivos csv y chequear consistencia
def load_all(file_personas, file_trabajadores, file_usuarios, file_peliculas, file_scores):
    # Inicializacion de dataframes
    df_personas = pd.read_csv(file_personas)
    df_trabajadores = pd.read_csv(file_trabajadores)
    df_usuarios = pd.read_csv(file_usuarios)
    df_peliculas = pd.read_csv(file_peliculas)
    df_scores = pd.read_csv(file_scores, )

    # Chequeo de consistencia
    print('Checking consistency.....')
    time.sleep(1)
    consistency_check(df_personas, df_trabajadores, 'id', file_trabajadores, 'Personas-Trabajadores')
    consistency_check(df_personas, df_usuarios, 'id', file_usuarios, 'Personas-usuarios')
    consistency_check(df_peliculas, df_scores, 'movie_id', file_scores, 'Peliculas-Scores')
    consistency_check(df_usuarios, df_scores, 'user_id', file_scores, 'Usuarios-Scores')
    print('Consistency checked')

    # Código de Carga
    return df_personas, df_trabajadores, df_usuarios, df_peliculas, df_scores


load_all(PERSONAS_CSV_ROUTE, TRABAJADORES_CSV_ROUTE, USERS_CSV_ROUTE, PELICULAS_CSV_ROUTE, SCORES_CSV_ROUTE)
