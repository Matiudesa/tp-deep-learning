import matplotlib.pyplot as plt
import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def peliculas_genero(data):
    genre_columns = data.columns[5:]
    movies_per_genre = data[genre_columns].sum()

    plt.figure(figsize=(10, 6))
    movies_per_genre.sort_values().plot(kind='barh', color='skyblue')
    plt.xlabel('Número de películas')
    plt.ylabel('Género')
    plt.title('Número de películas por género')
    plt.show()

    return movies_per_genre

def peliculas_fechas(data):
    genre_columns = data.columns[5:]

    data['Release Date'] = pd.to_datetime(data['Release Date'], errors='coerce')

    data['Release Year'] = data['Release Date'].dt.year

    movies_per_year = data['Release Year'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    movies_per_year.plot(kind='bar', color='skyblue')
    plt.xlabel('Release Year')
    plt.ylabel('Number of Movies')
    plt.title('Number of Movies Released Each Year')
    plt.xticks(rotation=90)
    plt.show()

    return movies_per_year

data = load_data('data/peliculas.csv')

peliculas_genero(data)

peliculas_fechas(data)
