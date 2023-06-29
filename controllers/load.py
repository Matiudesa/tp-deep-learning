import pandas as pd
from peliculas import PELICULAS_CSV_ROUTE
from personas import PERSONAS_CSV_ROUTE
from trabajadores import TRABAJADORES_CSV_ROUTE
from users import USERS_CSV_ROUTE
from scores import SCORES_CSV_ROUTE 

def load_all(file_personas, file_trabajadores, file_usuarios, file_peliculas, file_scores):

    # Inicializacion de dataframes
    df_personas = pd.read_csv(file_personas)
    df_trabajadores = pd.read_csv(file_trabajadores)
    df_usuarios = pd.read_csv(file_usuarios)
    df_peliculas = pd.read_csv(file_peliculas)
    df_scores = pd.read_csv(file_scores)

    #Cheque consistencia entre Personas, trabajadores y usuarios

    if df_usuarios['id'].isin(df_personas['id']).all():
        print('all users OK')
    else:
        print('NOT OK')
    




    #Código de Carga
    #return df_personas, df_trabajadores, df_usuarios, df_peliculas, df_scores


load_all(PERSONAS_CSV_ROUTE, TRABAJADORES_CSV_ROUTE, USERS_CSV_ROUTE, PELICULAS_CSV_ROUTE, SCORES_CSV_ROUTE)