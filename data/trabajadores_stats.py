import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    data_trabajadores = pd.read_csv('data/trabajadores.csv')
    return data_trabajadores

def position_distribution(data_trabajadores):
    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 6))
    sns.countplot(data=data_trabajadores, y='Position')
    plt.xlabel('Cantidad')
    plt.ylabel('Posicion')
    plt.title('Distribución de las posiciones')
    plt.show()

def category_distribution(data_trabajadores):
    sns.set(style="whitegrid")

    plt.figure(figsize=(6, 4))
    sns.countplot(data=data_trabajadores, x='Category')
    plt.xlabel('Categoria')
    plt.ylabel('Cantidad')
    plt.title('Distribución de las categorías')
    plt.show()

def working_hours_distribution(data_trabajadores):
    sns.set(style="whitegrid")

    plt.figure(figsize=(6, 4))
    sns.countplot(data=data_trabajadores, x='Working hours')
    plt.xlabel('Horas de trabajo')
    plt.ylabel('Cantidad')
    plt.title('Distribución de las horas de trabajo')
    plt.xticks(rotation=45)
    plt.show()

data_trabajadores = load_data()

position_distribution(data_trabajadores)

category_distribution(data_trabajadores)

working_hours_distribution(data_trabajadores)
