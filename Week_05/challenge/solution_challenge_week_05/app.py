from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

# Set global Matplotlib style for dark background
plt.style.use('dark_background')

# Set matplotlib backend to Agg
matplotlib.use('Agg')

# Initialize Flask app
app = Flask(__name__)

# Load the apartment data from CSV
@app.route('/')
def index():
    """Load the apartment data from CSV, calculate KPIs, 
       and render the HTML template.
    """
    
    # Load the CSV file (update the path if needed)
    df = pd.read_csv('../apartments_data_enriched_cleaned.csv')

    # Add ID column to the dataframe
    df['id'] = range(1, len(df) + 1)

    # Calculate KPIs and round them
    number_of_apartments = df.shape[0]
    mean_price = f"{df['price'].mean():.2f}"
    mean_area = f"{df['area'].mean():.2f}"

    # Plot histogram of prices (dark theme is applied globally)
    plt.figure(figsize=(10,6))
    
    # Plot the histogram with skyblue bars and white edges
    color = "#00CCCC"
    plt.hist(df['price'], bins=20, color=color, edgecolor="gray")
    
    # Set title and labels with greenyellow color
    plt.title('Price Distribution of Apartments', color='greenyellow')
    plt.xlabel('Price (CHF)', color='greenyellow')
    plt.ylabel('Number of Apartments', color='greenyellow')

    # Customize grid, tick parameters
    plt.grid(color='gray', linestyle='--')
    plt.tick_params(colors='greenyellow')

    # Save histogram to the static folder
    histogram_path = os.path.join('static', 'price_histogram.png')
    plt.savefig(histogram_path, bbox_inches='tight', transparent=True)
    plt.close()

    # Convert dataframe to a list of dictionaries
    apartments = df.to_dict(orient='records')

    # Render the index.html template and pass KPI data and histogram
    return render_template('index.html', apartments=apartments,
                           number_of_apartments=number_of_apartments, 
                           mean_price=mean_price, 
                           mean_area=mean_area, 
                           histogram_path=histogram_path)

if __name__ == '__main__':
    # Ensure the 'static' directory exists for storing the histogram image
    if not os.path.exists('static'):
        os.makedirs('static')

    # Run the Flask app
    app.run(debug=True)

