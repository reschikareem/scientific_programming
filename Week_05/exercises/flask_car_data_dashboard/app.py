import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template

# Set graphical parameters
plt.style.use('dark_background')
plt.rcParams.update({
    'text.color': 'greenyellow',
    'axes.labelcolor': 'greenyellow',
    'xtick.color': 'greenyellow',
    'ytick.color': 'greenyellow',
    'axes.edgecolor': 'greenyellow',
    'grid.color': 'greenyellow',
    'axes.titlecolor': 'greenyellow'
})

# Load the dataset
file_path = '../data/autoscout24_data_enriched_cleaned.csv'
df = pd.read_csv(file_path)

# Change columns to lower case and replace spaces with underscores
df.columns = df.columns.str.lower()

# Create the Flask app
app = Flask(__name__)

# Create the necessary plots and save them to the static folder
if not os.path.exists('static'):
    os.makedirs('static')

# 1. Histogram of price
plt.figure(figsize=(6, 4))
df['price'].hist(bins=30, color='skyblue', alpha=0.7)
plt.title('Histogram of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('static/histogram_price.png')
plt.close()

# 2. Bar chart of number of cars per fuel type
plt.figure(figsize=(6, 4))
df[df['fuel_type'].isin(['Elektro', 
                         'Diesel', 
                         'Benzin'])]['fuel_type'].value_counts().sort_values(ascending=True).plot(kind='barh', 
                                                                                                   color='skyblue', 
                                                                                                   alpha=0.7)
plt.title('Number of Cars per Fuel Type')
plt.xlabel('Count')
plt.ylabel('Fuel Type')
plt.savefig('static/barh_fuel_type.png')
plt.close()

# 3. Pie chart for selected fuel types
plt.figure(figsize=(6, 4))
df[df['fuel_type'].isin(['Diesel', 'Benzin', 'Elektro'])]['fuel_type'].value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['gold', 'skyblue', 'lightgreen']
)
plt.title('Distribution of Selected Fuel Types')
plt.ylabel('')
plt.savefig('static/pie_fuel_type.png')
plt.close()

# 4. Boxplot of mileage
plt.figure(figsize=(6, 4))
boxplot = df['mileage'].plot(kind='box', 
                            color='yellow',
                             vert=False, 
                             patch_artist=True, 
                             flierprops=dict(markerfacecolor='yellow', 
                                             markeredgecolor='yellow', 
                                             marker='o'),
                            medianprops=dict(color='gray'))
plt.title('Boxplot of Mileage')
plt.xlabel('Mileage')
plt.xticks(color='greenyellow')
plt.yticks(color='greenyellow')
plt.savefig('static/boxplot_mileage.png')
plt.close()

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

# HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Data Graphics</title>
    <style>
        body {
            background-color: black;
            color: greenyellow;
        }
    </style>
</head>
<body>
    <h1>Car Data Dashboard</h1>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 5px;">
        <div><img src="/static/histogram_price.png" alt="Histogram of Price" style="width: 60%;"></div>
        <div><img src="/static/barh_fuel_type.png" alt="Bar Chart of Fuel Types" style="width: 60%;"></div>
        <div><img src="/static/pie_fuel_type.png" alt="Pie Chart of Fuel Types" style="width: 60%;"></div>
        <div><img src="/static/boxplot_mileage.png" alt="Boxplot of Mileage" style="width: 60%;"></div>
    </div>
</body>
</html>"""

# Write the HTML template to the templates folder
if not os.path.exists('templates'):
    os.makedirs('templates')

with open('templates/index.html', 'w') as f:
    f.write(html_template)

if __name__ == '__main__':
    app.run(debug=True)
