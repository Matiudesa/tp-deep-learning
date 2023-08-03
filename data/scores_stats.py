import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    data_scores = pd.read_csv('tp-deep-learning\data\scores.csv')
    return data_scores

def ratings_distribution(data_scores):
    sns.set(style="whitegrid")

    plt.figure(figsize=(6, 4))
    sns.countplot(data=data_scores, x='rating')
    plt.xlabel('Rating')
    plt.ylabel('Cantidad')
    plt.title('Distribución del rating')
    plt.show()

def ratings_per_user_distribution(data_scores):
    sns.set(style="whitegrid")

    ratings_per_user = data_scores['user_id'].value_counts()

    plt.figure(figsize=(10, 6))
    sns.histplot(ratings_per_user, bins=30, kde=True, color='skyblue')
    plt.xlabel('Número de ratings por usuarios')
    plt.ylabel('Cantidad')
    plt.title('distribuciónde número de ratings por usuarios')
    plt.show()

data_scores = load_data()

ratings_distribution(data_scores)

ratings_per_user_distribution(data_scores)
