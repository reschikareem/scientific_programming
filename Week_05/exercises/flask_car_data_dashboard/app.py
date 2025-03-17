"""
This module creates a Flask app that displays a dashboard with four plots. 
Different plots are created and saved as images in the static folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template

# Set graphical parameters
plt.style.use('dark_background')
plt.rcParams.update({
    'text.color': 'black',
    'axes.labelcolor': 'greenyellow',
    'xtick.color': 'greenyellow',
    'ytick.color': 'greenyellow',
    'axes.edgecolor': 'greenyellow',
    'grid.color': 'greenyellow',
    'axes.titlecolor': 'greenyellow'
})

# Read the dataset
FILE_PATH = '../data/autoscout24_data_enriched_cleaned.csv'
df = pd.read_csv(FILE_PATH)

# Change columns to lower case and replace spaces with underscores
df.columns = df.columns.str.lower()

# Create the Flask app
app = Flask(__name__)

# Create histogram
plt.figure(figsize=(6, 4))
df['price'].hist(bins=30, color='skyblue', alpha=0.7)
plt.title('Histogram of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('static/histogram_price.png')
plt.close()

# Create bar chart
plt.figure(figsize=(6, 4))
df[df['fuel_type'].isin(['Elektro',
                         'Diesel',
                         'Benzin'])]['fuel_type'].value_counts().sort_values(
    ascending=True).plot(kind='barh', color='skyblue', alpha=0.7)
plt.title('Number of Cars per Fuel Type')
plt.xlabel('Count')
plt.ylabel('Fuel Type')
plt.savefig('static/barh_fuel_type.png')
plt.close()

# Create pie chart
plt.figure(figsize=(6, 4))
df[df['fuel_type'].isin(['Diesel',
                         'Benzin',
                         'Elektro'])]['fuel_type'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=140,
    colors=['gold', 'skyblue', 'lightgreen'],
    textprops={'color': 'black'}
)
plt.title('Distribution of Selected Fuel Types')
plt.ylabel('')
plt.legend(labels=['Diesel', 'Benzin', 'Elektro'], 
           loc='upper right',
           labelcolor='greenyellow')
plt.savefig('static/pie_fuel_type.png')
plt.close()

# Create boxplot
plt.figure(figsize=(6, 4))
boxplot = df['mileage'].plot(kind='box',
                             color='yellow',
                             vert=False,
                             patch_artist=True,
                             flierprops={'markerfacecolor': 'yellow',
                                         'markeredgecolor': 'yellow',
                                         'marker': 'o'},
                             medianprops={'color': 'gray'})
plt.title('Boxplot of Mileage')
plt.xlabel('Mileage')
plt.xticks(color='greenyellow')
plt.yticks(color='greenyellow')
plt.savefig('static/boxplot_mileage.png')
plt.close()

# Define the routes
@app.route('/')
def index():
    """Return the index.html template."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
