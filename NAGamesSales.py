import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data = pd.read_csv('vgsales.csv')

# Trier les données par ventes en Amérique du Nord (NA_Sales) dans l'ordre décroissant
top_na_games = data.sort_values(by='NASales', ascending=False).head(10)

# Afficher un graphique à barres pour les 100 jeux les plus vendus au NA
plt.figure(figsize=(12, 6))
plt.bar(top_na_games['Name'], top_na_games['NASales'], color='green')
plt.xlabel('Jeux')
plt.ylabel('Ventes en Amérique du Nord')
plt.title('Top 10 des jeux les plus vendus aux États-Unis')
plt.xticks(rotation=90)
plt.show()
