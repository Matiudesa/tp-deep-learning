import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def load_data():
    data_personas = pd.read_csv('tp-deep-learning\data\personas.csv')
    return data_personas

def personas_generos(data_personas):
    sns.set(style="whitegrid")

    missing_values_personas = data_personas.isnull().sum()

    total_people = data_personas.shape[0]

    gender_distribution = data_personas['Gender'].value_counts()

    plt.figure(figsize=(6, 4))
    sns.countplot(data=data_personas, x='Gender')
    plt.xlabel('Genero')
    plt.ylabel('Cantidad')
    plt.title('Distribución de la cantidad de personas por género')
    plt.show()

def personas_edades(data_personas):
    sns.set(style="whitegrid")

    current_year = datetime.now().year
    data_personas['Age'] = current_year - data_personas['year of birth']

    age_distribution = data_personas['Age'].describe()

    plt.figure(figsize=(10, 6))
    sns.histplot(data_personas['Age'], bins=30, kde=True, color='skyblue')
    plt.xlabel('Edad')
    plt.ylabel('Cantidad')
    plt.title('Distribución de la edad')
    plt.show()

data_personas = load_data()

personas_generos(data_personas)

personas_edades(data_personas)
