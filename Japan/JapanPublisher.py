import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis votre fichier CSV
data = pd.read_csv('vgsales.csv')

# Trier les données par ventes au Japon
data_sorted = data.sort_values(by='JP_Sales', ascending=False)

# Sélectionner les 50 premiers éditeurs
top_publishers = data_sorted.head(1000)

# Sélectionner les noms des éditeurs et leurs ventes au Japon
publishers = top_publishers['Publisher']
jp_sales = top_publishers['JP_Sales']

# Créer un graphique à barres pour visualiser les ventes au Japon par éditeur
plt.figure(figsize=(12, 8))
plt.bar(publishers, jp_sales, color='blue')
plt.xticks(rotation=90)  # Rotation des étiquettes pour une meilleure lisibilité
plt.xlabel('Éditeur', fontsize=12)
plt.ylabel('Ventes au Japon en millions', fontsize=12)
plt.title('Top 50 des Éditeurs par Ventes au Japon', fontsize=16)
plt.tight_layout()
plt.show()
