import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV (à adapter à votre fichier)
data = pd.read_csv('vgsales.csv')

# Sélectionner les 10 jeux les plus vendus en "JP_Sales"
top_10_jp_sales = data.nlargest(10, 'JP_Sales')

# Créer un graphique camembert
plt.figure(figsize=(8, 8))
plt.pie(top_10_jp_sales['JP_Sales'], labels=top_10_jp_sales['Name'], autopct='%1.1f%%', startangle=140)
plt.title('Répartition des 10 jeux les plus vendus au Japon')
plt.axis('equal')  # Pour que le camembert soit un cercle

# Afficher le graphique
plt.show()
