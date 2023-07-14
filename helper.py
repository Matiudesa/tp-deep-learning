"""
-Load.py
#
def consistency_check(df_base, df_check, column, file, check_name)
# Esta función checkea la consistencia de los dataframes comparando los valores de una columna específica y elimina las filas en el df_check que no estén en el df_check que no cumplen con la verificación.
# Luego, guarda el DataFrame resultante en un archivo CSV y muestra un mensaje de confirmación.



def load_all(file_personas, file_trabajadores, file_usuarios, file_peliculas, file_scores)
# Esta función carga múltiples archivos CSV y chequea la consistencia de los dataframes entre ellos.


-Peliculas.py
#
@classmethod
def create_df_from_csv(cls, filename):
# Esta función crea un dataframe Peliculas con la información proveniente de un archivo .csv, completando donde haya NaN y devuelve un dataframe con la información.

#
@classmethod    
def get_from_df(cls, df_peliculas, id=None, nombre = None, anios = None, generos = None) -> pd.DataFrame:
# Esta función filtra un dataframe de Películas de acuerdo a los criterios en los argumentos y devuelve otro dataframe.

#
@classmethod
def get_stats(cls, df_peliculas, anios=None, generos=None) -> None:
# Esta función devuelve las estadísticas sobre dataframe Películas ingresado, de acuerdo a el rango de años y género en los argumentos.
# Se muestra la película más antigua y más reciente. Luego genera dos gráficas: Oelículas por año y Películas por género.

#
def write_df(self, df_peliculas, overwrite=False) -> None:
# Esta función permite actualizar el archivo CSV con la información del Dataframe como argumento. Por defecto, no sobreescribirá si existe el ID de Película en archivo, para hacerlo ingresar overwrite = True.

#
def remove_from_df(self, df_peliculas) -> None:
# Esta función permite eliminar un registro del Dataframe. Si encuentra un registro que coincide con todas las propiedades, elimina esa fila del DataFrame y guarda los cambios en el archivo CSV. 
# Si no se encuentra el registro, devuelve un error.


-Personas.py
#
def get_age(self) -> int:
# Este método retorna el año de nacimiento a partir de la fecha de nacimiento

#
@classmethod
def create_df_from_csv(cls, filename) -> pd.DataFrame:
# Esta función crea y devuelve un dataframe de Personas con la información proveniente de un archivo .csv.

#
@classmethod
def get_from_df(cls, df_mov, id=None, nombre=None, anios=None, generos=None) -> pd.DataFrame:
# Esta función filtra un dataframe de Personas de acuerdo a los criterios en los argumentos y devuelve otro dataframe.

#
@classmethod
def get_stats(cls, df_personas, anios=None, generos=None) -> None:
# Esta función devuelve las estadísticas sobre dataframe Personas ingresado, de acuerdo a el rango de años y género en los argumentos.
# Crea un histograma para cada género de la cantidad nacida de hombres y mujeres por año, siempre y cuando lo años y generos no se especifiquen.


#
def write_df(self, df_personas, overwrite=False) -> None:
# Esta función permite actualizar el archivo CSV con la información del Dataframe como argumento. 
# Si no se especifica un ID en el dataframe Personas se generará uno nuevo a continuación del último.
# Si el ID especificado existe, sobreescribirá el registro sólo en caso que overwrite=True, caso contrario devuelve un mensaje de error.

#
def remove_from_df(self, df_peliculas) -> None:
# Esta función permite eliminar un registro del Dataframe. Si encuentra un registro que coincide con todas las propiedades, elimina esa fila del DataFrame y guarda los cambios en el archivo CSV. 
# Si no se encuentra el registro, devuelve un error.


-Save.py
#
def save_all():
# Esta función guarda todos los archivos CSV en la ruta especificada.


-Scores.py
#
@classmethod
def create_df_from_csv(cls, filename: str) -> pd.DataFrame:
# Esta función crea y devuelve un dataframe de Scores con la información proveniente de un archivo CSV.

#
@classmethod
def get_from_df(cls, df_scores, usuario_id=None, pelicula_id=None, puntuacion=None) -> pd.DataFrame:
# Esta función filtra un dataframe de Scores de acuerdo a los criterios en los argumentos y devuelve otro dataframe filtrado.

#
def write_df(self, df_scores, overwrite=False) -> None:
# Esta función permite actualizar el archivo CSV con la información del Dataframe como argumento. 
# Primero checkea si existen los ID de Usuario y de Película, devolviendo un mensaje de error en caso de que no sea así.
# Remueve los milisegundos del Timestamp correspondiente.
# Luego si overwrite = True, actualiza la puntuación correspondiente en el archivo CSV. Caso contrario agrega una nueva línea en el dataframe Scores y actualiza el CSV de Puntuaciones.


#
def remove_from_df(self, df_scores) -> None:
# Esta función elimina una entrada del dataframe Scores si coincide el usuario, película y puntuación, no por timestamp.
# Si coincide elimina y actualiza el archivo CSV.

#
@staticmethod
def get_user_avg(df_scores) -> pd.DataFrame:
# Devuelve la media de los puntajes agrupados por Usuario


#
@staticmethod
def get_movie_avg(df_scores) -> pd.DataFrame:
# Devuelve la media de los puntajes agrupados por Película

@staticmethod
def get_user_avg_by_id(df_scores, user_id) -> pd.DataFrame:
# Calcula el promedio de puntuaciones de un usuario específico por ID.


@staticmethod
def get_movie_avg_by_id(df_scores, movie_id) -> int:
# Calcula el promedio de puntuaciones de una determinada película y devuelve un número entero a partir del resultado.

-Trabajadores.py

#
@classmethod
def create_df_from_csv(cls, filename) -> pd.DataFrame:
# Esta función crea y devuelve un dataframe de Trabajadores con la información proveniente de un archivo CSV.

#
@classmethod
def get_from_df(cls, df_trabajadores , fechas = None, puesto=None, horario_trabajo=None, categoria=None) -> pd.DataFrame:
# Esta función filtra un dataframe de Trabajadores de acuerdo a los criterios en los argumentos y devuelve otro dataframe filtrado.

#
@classmethod
def get_stats(cls, df_trabajadores, puesto = None) -> None:
# Si se especifica el argumento Puesto, devuelve la cantidad de trabajadores en dicho puesto. Sino devuelve la cantidad total de trabajadores.
# Luego genera un gráfico de torta donde muestra la Cantidad de trabajadores por puesto.

#
def write_df(self, df_trabajadores, overwrite = False) -> None: 
# Esta función permite actualizar el archivo CSV de Trabajadores.
# Primero verifica que el ID exista en el dataframe Personas, de donde hereda la clase, y sino devuelve error.
# Luego si overwrite=True entonces verifica que exista el ID en el registro Trabajadores y lo actualiza, caso contrario devuelve error.
# Si overwrite= False, entonces crea un nuevo trabajador y actualiza el archivo CSV. En caso de que el ID ya exista, devuelve error.
# En todos los casos devuelve error si no se especifica un ID de Persona correspondiente.

#
def remove_from_df(self, df_trabajadores) -> None:
# Esta función elimina una entrada del dataframe  Trabajadores, si coinciden todos los campos del trabajador con lo guardado.
# Si coincide elimina y actualiza el archivo CSV.

-Users.py

#
def add_user(self, id, occupation, active_since, overwrite=False):
# Agrega un nuevo usuario. 
# Primero la función verifica que exista el ID de persona correspondiente. Sino devuelve error.
# Si overwrite = True, entonces actualiza el usuario según el ID recibido junto con el CSV, en caso de existir. Caso contrario devuelve error.
# Si overwrte = False, agrega un nuevo usuario a continuación del último y actualiza el CSV correspondiente.

#
@classmethod
def create_df_from_csv(cls, filename):
# Esta función crea y devuelve un dataframe de Usuarios con la información proveniente de un archivo CSV.

#
@classmethod
def get_from_df(cls, df, id=None, occupation=None, active_since=None):
# Esta función filtra un dataframe de Usuarios de acuerdo a los criterios en los argumentos y devuelve otro dataframe filtrado.

#
@classmethod
def get_stats(cls, df, occupations=None, birth_year=None, min_users=None):
# Esta función realiza estadísticas sobre el dataframe de Usuarios según los criterios proporcionados, fecha de nacimiento y ocupación.
# Muestra cantidad de usuarios totales, por ocupación y luego en caso de que se especifique, si cumple o no el criterio de que exista una cantidad mínima de usuarios.

#
def remove_from_df(self, df):
# Esta función elimina una entrada del dataframe  Usuarios, si se encuentra el ID correspondiente.
# Si coincide elimina y actualiza el archivo CSV.

"""
