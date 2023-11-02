import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV (à adapter à votre fichier)
data = pd.read_csv('vgsales.csv')

# Regrouper les données par genre et calculer les ventes totales au Japon
genre_jp_sales = data.groupby('Genre')['JP_Sales'].sum()

# Sélectionner le genre avec les ventes totales les plus élevées au Japon
most_popular_genre_jp = genre_jp_sales.idxmax()

# Créer un graphique à barres
plt.figure(figsize=(10, 6))
plt.bar(genre_jp_sales.index, genre_jp_sales.values, color='m')
plt.xlabel('Genre')
plt.ylabel('Ventes totales au Japon')
plt.title(f'Genre de jeu le plus consommé par les joueurs japonais (Genre le plus populaire: {most_popular_genre_jp})')
plt.xticks(rotation=45)
plt.tight_layout()

# Afficher le graphique
plt.show()
