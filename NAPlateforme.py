import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data = pd.read_csv('vgsales.csv')

# Regrouper les données par plateforme et calculer les ventes totales en Amérique du Nord
platform_sales = data.groupby('Platform')['NASales'].sum().reset_index()

# Trier les plateformes en fonction des ventes en Amérique du Nord (NA_Sales) dans l'ordre décroissant
platform_sales = platform_sales.sort_values(by='NASales', ascending=False)

# Afficher un graphique à barres montrant les plateformes les plus vendues au NA
plt.figure(figsize=(12, 6))
plt.bar(platform_sales['Platform'], platform_sales['NASales'], color='blue')
plt.xlabel('Plateforme')
plt.ylabel('Ventes en Amérique du Nord (NASales)')
plt.title('Plateformes les plus vendues aux États-Unis')
plt.xticks(rotation=90)
plt.show()
