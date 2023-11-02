import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV (à adapter à votre fichier)
data = pd.read_csv('vgsales.csv')

# Regrouper les données par plateforme et calculer les ventes totales au Japon
platform_jp_sales = data.groupby('Platform')['JP_Sales'].sum()

# Sélectionner la plateforme avec les ventes totales les plus élevées au Japon
most_popular_platform_jp = platform_jp_sales.idxmax()

# Créer un graphique à barres
plt.figure(figsize=(10, 6))
plt.bar(platform_jp_sales.index, platform_jp_sales.values, color='c')
plt.xlabel('Plateforme')
plt.ylabel('Ventes totales au Japon')
plt.title(f'Plateforme la plus utilisée par les joueurs japonais (Meilleure plateforme: {most_popular_platform_jp})')
plt.xticks(rotation=45)
plt.tight_layout()

# Afficher le graphique
plt.show()
