from flask import Flask, request, jsonify, render_template
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import nltk

# Download necessary NLTK datasets
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize Flask app
app = Flask(__name__)

# Initialize Lemmatizer and Stopwords
lemmatizer = WordNetLemmatizer()
try:
    stop_words = set(stopwords.words('english'))
except Exception as e:
    print("Error loading stopwords:", e)
    stop_words = set()

# Feature Extraction Function
def extract_features(text):
    try:
        tokens = word_tokenize(text)
        lower_case_tokens = [token.lower() for token in tokens]
        features = {
            lemmatizer.lemmatize(token): True
            for token in lower_case_tokens
            if token not in stop_words and token not in string.punctuation
        }
        return features
    except Exception as e:
        print("Error extracting features:", e)
        return {}

# Load the pre-trained model
try:
    with open("sentiment_model.pkl", "rb") as model_file:
        classifier = pickle.load(model_file)
except FileNotFoundError:
    print("Error: 'sentiment_model.pkl' not found. Please ensure the model file is in the correct path.")
    classifier = None
except Exception as e:
    print("Error loading model:", e)
    classifier = None

# Home route to serve HTML
@app.route('/')
def index():
    return render_template('index.html')

# Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    if classifier is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.json
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        sentiment = classifier.classify(extract_features(text))
        return jsonify({"text": text, "sentiment": sentiment})
    except Exception as e:
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
