"""
This Flask application generates a histogram based on user input.
"""

# Import libraries
import io
import base64
import warnings
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, redirect, url_for, flash

# Set matplotlib backend to Agg
matplotlib.use('Agg')

# Set dark background theme for plots
plt.style.use('dark_background')

# Ignore warnings
warnings.filterwarnings('ignore')

# Flask app setup
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route for the Flask application
    """
    if request.method == 'POST':
        try:
            # Safely retrieve form data with defaults
            obs = int(request.form.get('obs', 100))  # Default: 100
            mean = float(request.form.get('mean', 0))  # Default: 0
            stddev = float(request.form.get('stddev', 1))  # Default: 1

            if obs <= 0 or stddev <= 0:
                flash(
                    "Observations and standard deviation must be positive numbers.", "error")
                return redirect(url_for('index'))

            # Generate random data for the histogram
            data = np.random.normal(mean, stddev, obs)

            # Create histogram
            fig, ax = plt.subplots(figsize=(7, 5))
            ax.hist(data, bins=50, color="greenyellow", alpha=0.8)
            ax.set_xlabel('Value', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            ax.set_title('Histogram', fontsize=14)

            # Save plot to in-memory image
            img = io.BytesIO()
            fig.tight_layout()
            fig.savefig(img, format='png')
            img.seek(0)
            plt.close(fig)

            # Encode plot to base64
            plot_url = base64.b64encode(img.getvalue()).decode()

            return render_template('index.html', plot_url=plot_url)

        except ValueError:
            flash("Invalid input. Please enter valid numerical values.", "error")
            return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
