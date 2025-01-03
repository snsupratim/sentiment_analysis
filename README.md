# Sentiment Analysis Web Application

A simple web application that uses Natural Language Processing (NLP) to analyze the sentiment of user-input text. It leverages a machine learning model trained to classify text into positive or negative sentiments. Built with Flask and NLTK, this app allows users to input text and receive real-time sentiment analysis results.

## Features

- **Real-time Sentiment Analysis**: Analyze the sentiment of a sentence (positive or negative) by inputting it into a text box.
- **User-Friendly Interface**: Clean and responsive UI with a simple text input and a button to submit the text for analysis.
- **Color-Coded Results**: Sentiment results are displayed with corresponding colors and emoji feedback for a more engaging experience.

## Requirements

- Python 3.7 or higher
- Flask
- NLTK (Natural Language Toolkit)
- Pickle (for loading the pre-trained sentiment analysis model)

## Installation

### Clone the repository:

```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Download necessary NLTK data:

If you haven't already downloaded the required NLTK data (like `punkt`, `wordnet`, and `stopwords`), the application will automatically attempt to download them when run. Alternatively, you can manually download them using:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
```

### Ensure model availability:

Make sure the trained model file (`sentiment_model.pkl`) is available in the root directory of the project.

## Usage

### Run the Flask Application:

```bash
python app.py
```

### Access the application:

Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Analyze Sentiment:

1. Input a sentence into the provided text box.
2. Click the **Analyze Sentiment** button.
3. View the sentiment result: The application will display whether the sentiment is **Positive** or **Negative**, along with corresponding emojis.

## File Structure

```plaintext
/project-folder
├── app.py                   # Main Flask application
├── sentiment_model.pkl      # Pre-trained sentiment analysis model
├── templates/
│   └── index.html           # Front-end HTML page
└── nltk_data/               # (Optional) NLTK data directory
```

## Notes

- Ensure that the file `sentiment_model.pkl` (your trained sentiment model) is available in the project folder for the app to work correctly.
- This app currently supports basic sentiment analysis (positive/negative) and does not handle neutral sentiments.
- You can expand this project by improving the model or adding more functionalities, such as multi-language support or a more complex sentiment scale (e.g., very positive, very negative).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Built with ❤️ by snsupratim
