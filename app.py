from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load your data and model
df = pd.read_csv("cosmetics.csv")
tsne_features = joblib.load('tsne_features.pkl')

# Prepare moisturizers for dry skin
moisturizers = df[df['Label'] == 'Moisturizer']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    skin_type = request.form['skin_type']

    if skin_type == 'Dry':
        moisturizers_dry = moisturizers[moisturizers['Dry'] == 1]
        recommended = moisturizers_dry.sample(5, random_state=42)
    elif skin_type == 'Oily':
        moisturizers_dry = moisturizers[moisturizers['Oily'] == 1]
        recommended = moisturizers_dry.sample(5, random_state=42)
    elif skin_type == 'Combination':
        moisturizers_dry = moisturizers[moisturizers['Combination'] == 1]
        recommended = moisturizers_dry.sample(5, random_state=42)
    elif skin_type == 'Normal':
        moisturizers_dry = moisturizers[moisturizers['Normal'] == 1]
        recommended = moisturizers_dry.sample(5, random_state=42)
    elif skin_type == 'Sensitive':
        moisturizers_dry = moisturizers[moisturizers['Sensitive'] == 1]
        recommended = moisturizers_dry.sample(5, random_state=42)
    else:
        recommended = moisturizers.sample(5, random_state=42)

    products = []
    for idx, row in recommended.iterrows():
        products.append({
            'Name': row['Name'],
            'Brand': row['Brand'],
            'Price': row['Price'],
            'Ingredients': row['Ingredients'][:100] + "..."
        })

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
