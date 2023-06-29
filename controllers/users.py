import pandas as pd
from datetime import datetime
from personas import Personas, PERSONAS_CSV_ROUTE

class UserManagement(Personas):
    def __init__(self, nombre, fecha_nacimiento, genero, codigo_postal, dataframe, csv_filename, id=None):
        super().__init__(nombre, fecha_nacimiento, genero, codigo_postal, id)
        self.dataframe = dataframe
        self.csv_filename = csv_filename

    def __repr__(self):
        return self.dataframe.to_string(index=False)

    def add_user(self, id, occupation, active_since):
        new_user = pd.DataFrame([[id, occupation, active_since]], columns=self.dataframe.columns)
        self.dataframe = pd.concat([self.dataframe, new_user], ignore_index=True)

        # Guardar los cambios en el archivo CSV
        self.dataframe.to_csv(self.csv_filename, index=False)

    def remove_user(self, id):
        self.dataframe = self.dataframe[self.dataframe['id'] != id]

        # Guardar los cambios en el archivo CSV
        self.dataframe.to_csv(self.csv_filename, index=False)

    @classmethod
    def create_df_from_csv(cls, filename):
        df = pd.read_csv(filename)
        df['Active Since'] = pd.to_datetime(df['Active Since'].str[:10], format='%Y-%m-%d')
        return df

    @classmethod
    def get_from_df(cls, df, id=None, occupation=None, active_since=None):
        query = []

        if id is not None:
            query.append(f'id == {id}')

        if occupation is not None:
            query.append(f'Occupation == "{occupation}"')

        if active_since is not None:
            query.append(f'`Active Since` == "{active_since}"')

        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df.query(query_str)
        else:
            result_df = df

        return result_df

    @classmethod
    def get_stats(cls, df, occupations=None, birth_year=None, min_users=None):
        query = []

        if occupations is not None:
            occupations_query = ' or '.join([f'Occupation.str.contains("{occupation}")' for occupation in occupations])
            query.append(f'({occupations_query})')

        if birth_year is not None:
            birth_year_query = f'`Active Since`.dt.year == {birth_year}'
            query.append(birth_year_query)

        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df.query(query_str)
        else:
            result_df = df

        if result_df.empty:
            print("No se encontraron usuarios que cumplan los requisitos.")
            return

        print("Cantidad total de usuarios:", len(result_df))

        print("\nCantidad de usuarios por ocupación:")
        print(result_df['Occupation'].value_counts())

        if min_users is not None:
            users_count = result_df.shape[0]
            if users_count >= min_users:
                print(f"\nLa cantidad de usuarios ({users_count}) cumple el requisito mínimo de {min_users} usuarios.")
            else:
                print(f"\nLa cantidad de usuarios ({users_count}) no cumple el requisito mínimo de {min_users} usuarios.")

    def remove_from_df(self, df):
        matching_rows = df[df['id'] == self.id]

        if matching_rows.empty:
            raise ValueError("No se encontró el usuario en el DataFrame.")

        df = df.drop(matching_rows.index)
        return df


# Nombre del archivo CSV
USERS_CSV_ROUTE = 'data/usuarios.csv'

# Cargar el DataFrame existente desde el archivo CSV
df_usuarios = UserManagement.create_df_from_csv(USERS_CSV_ROUTE)

# Obtener estadísticas de usuarios por ocupación y filtrar por año de nacimiento y cantidad de usuarios
#UserManagement.get_stats(df_usuarios, occupations=['technician', 'educator'], birth_year=1997, min_users=5)

user_manager = UserManagement(
    nombre='John Doe',
    fecha_nacimiento='1990-05-15',
    genero='M',
    codigo_postal='12345',
    dataframe=df_usuarios,  # DataFrame existente
    csv_filename=USERS_CSV_ROUTE  # Nombre del archivo CSV
)

'''
user_manager.add_user(
    id=944,
    occupation='engineer',
    active_since='2023-01-01'
)
'''
# user_manager.remove_user(id=944)
