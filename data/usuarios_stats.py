import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    data_usuarios = pd.read_csv('data/usuarios.csv')
    return data_usuarios

def occupation_distribution(data_usuarios):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data_usuarios, y='Occupation')
    plt.xlabel('Cantidad')
    plt.ylabel('Ocupación')
    plt.title('Distribución de la ocupación')
    plt.show()

data_usuarios = load_data()

occupation_distribution(data_usuarios)
