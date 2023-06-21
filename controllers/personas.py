from abc import ABC, abstractmethod
import pandas as pd
from datetime import datetime
from dtos.personasDTO import PersonaDTO


class Personas(PersonaDTO, ABC):

    def __repr__(self):
        string = list()
        string.append(f'ID: {self.id}')
        string.append(f'Fecha nacimiento: {self.fecha_nacimiento}')
        string.append(f'Genero: {self.genero}')
        string.append(f'Codigo postal: {self.codigo_postal}')
        return "\n".join(string)

    @classmethod
    def create_df_from_csv(cls, filename):
        df_mov = pd.read_csv(filename)
        return df_mov

    @classmethod
    def get_from_df(cls, df_mov, id=None, nombre=None, anios=None, generos=None):
        query = []

        if (id != None):
            query.append(f'id == {id} ')
        if (nombre != None):
            query.append(f' `Full Name` == "{nombre}" ')
        if (anios != None):
            today = datetime.today()
            year_from_age = today.year - anios
            query.append(f' `year of birth` == {year_from_age} ')
        if (generos != None):
            query.append(f'Gender == "{generos}" ')

        if len(query) > 0:
            query_str = ' and '.join(query)
            result_df = df_mov.query(query_str)
        else:
            result_df = df_mov

        return result_df

    # @abstractmethod
    # def write_df(self):
    #  pass

    def get_stats(cls, df_mov, anios=None, generos=None):
        pass

    def remove_from_df(self, df_mov):
        pass


filename = '../data/personas.csv'


