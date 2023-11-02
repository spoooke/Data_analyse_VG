import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV (à adapter à votre fichier)
data = pd.read_csv('vgsales.csv')

# Sélectionner les 10 jeux les plus vendus en global sales
top_10_games = data.nlargest(10, 'Global_Sales')

# Créer un graphique
plt.figure(figsize=(10, 6))
plt.barh(top_10_games['Name'], top_10_games['Global_Sales'], color='royalblue')
plt.xlabel('Ventes globales en millions')
plt.title('Les 10 jeux les plus vendus')
plt.gca().invert_yaxis()  # Pour avoir le jeu le plus vendu en haut

# Afficher le graphique
plt.show()
