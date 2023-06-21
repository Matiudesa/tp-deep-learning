from abc import ABC, abstractmethod
import pandas as pd
from datetime import datetime

class Persona(ABC):
    
   def __init__(self, fecha_nacimiento, genero, codigo_postal, id = None):
      self.id = id
      self.fecha_nacimiento = fecha_nacimiento
      self.genero = genero
      self.codigo_postal = codigo_postal

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
   def get_from_df(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
      query = []
      if(id != None):
         return df_mov[df_mov['id'] == id]
      elif(nombre != None):
         return df_mov[df_mov['Full Name'] == nombre]
      elif(anios != None):
         today = datetime.today()
         year_of_birth = today.year - anios
         return df_mov[df_mov['year of birth'] == year_of_birth]
      elif(generos != None):
         return df_mov[df_mov['generos'] == generos]
      else:
         return query

   @abstractmethod
   def write_df(self):
      pass

   def get_stats(cls,df_mov, anios=None, generos=None):
        pass
   
   def remove_from_df(self, df_mov):
      pass

filename = 'data/personas.csv'

df = Persona.create_df_from_csv(filename)
print(Persona.get_from_df(df, anios = 54))





    


  
