import numpy as np
from flask import Flask, request, render_template
import joblib

# Initialize the flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Create a list of the features in the correct order
    feature_list = [
        request.form.get('battery_power', type=float),
        request.form.get('blue', type=float),
        request.form.get('clock_speed', type=float),
        request.form.get('dual_sim', type=float),
        request.form.get('fc', type=float),
        request.form.get('four_g', type=float),
        request.form.get('int_memory', type=float),
        request.form.get('m_dep', type=float),
        request.form.get('mobile_wt', type=float),
        request.form.get('n_cores', type=float),
        request.form.get('pc', type=float),
        request.form.get('px_height', type=float),
        request.form.get('px_width', type=float),
        request.form.get('ram', type=float),
        request.form.get('sc_h', type=float),
        request.form.get('sc_w', type=float),
        request.form.get('talk_time', type=float),
        request.form.get('three_g', type=float),
        request.form.get('touch_screen', type=float),
        request.form.get('wifi', type=float)
    ]

    # Convert the list to a NumPy array for prediction
    final_features = [np.array(feature_list)]

    # Make a prediction
    prediction = model.predict(final_features)
    
    # Map the prediction to the readable class name
    price_ranges = ['Low Cost', 'Medium Cost', 'High Cost', 'Very High Cost']
    output = price_ranges[prediction[0]]

    # Render the HTML page with the prediction result
    return render_template('index.html', prediction_text=f'Predicted Price Range: {output}')

if __name__ == "__main__":
    app.run(debug=True)