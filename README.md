# Carify – Personalized Skincare Product Recommendation System

**Carify** is a machine learning–powered web application that recommends skincare products based on different skin types: **Combination, Dry, Normal, Oily, and Sensitive**. It combines natural language processing, dimensionality reduction, and interactive visualization to deliver a smart and user-friendly experience.

---

## 🔍 Features

- 🧴 Personalized skincare product recommendations  
- 📄 Text processing using Document-Term Matrix (DTM)  
- 🔡 Categorical encoding with One-Hot Encoder  
- 📉 Dimensionality reduction with t-SNE  
- 📊 Interactive visualization using Bokeh  
- 🌐 Flask backend with HTML/CSS/JavaScript frontend  

---

## 🧠 How It Works

1. **Text Vectorization**  
   Product descriptions are converted into a Document-Term Matrix using `CountVectorizer`.

2. **Categorical Encoding**  
   Skin types are transformed using `OneHotEncoder` for model input.

3. **Dimensionality Reduction**  
   `t-SNE` reduces feature dimensions for visualization.

4. **Visualization**  
   `Bokeh` displays t-SNE features as an interactive 2D plot.

5. **API & Frontend**  
   A Flask API serves predictions to a responsive HTML page that displays results and visuals.

---

## 🚀 Technologies Used

- Python (scikit-learn, joblib, Flask, Bokeh)
- HTML, CSS, JavaScript
- CountVectorizer, OneHotEncoder
- t-SNE for visualization

---

## 💡 Use Case

A user selects their skin type on the website. Carify recommends suitable skincare products and displays them on a visual 2D map, helping users understand product similarity and suitability.

---

## 📂 Project Structure
Carify

├── ▶ app.py                 → Flask backend

├── ▶ model.pkl              → Trained ML model (or use tsne_features.pkl)

├── ▶ tsne_features.pkl      → Saved t-SNE features for visualization

├── ▶ requirements.txt       → Python dependencies

├── 📁 templates/            → HTML templates

   └── ▶ index.html         → Frontend user interface
   
├── 📁 static/               → Static assets (CSS, JS, etc.)

    └── ▶ styles.css         → Styling for the web page



