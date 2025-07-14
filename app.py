from flask import Flask, request, render_template
from transformers import pipeline
from textblob import TextBlob

app = Flask(__name__)

# Load both models
transformers_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """Enhanced sentiment analysis with better positive detection"""
    # First analysis with Transformers
    result = transformers_model(text)[0]
    
    # Secondary check using TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # List of clearly positive phrases (add more as needed)
    positive_phrases = [
        "i like you", "i love", "it's great", "awesome", 
        "wonderful", "amazing", "fantastic"
    ]
    
    # Override to positive if text contains clearly positive phrases
    if any(phrase in text.lower() for phrase in positive_phrases):
        return {
            'label': 'POSITIVE',
            'score': 0.99  # High confidence
        }
    # Neutral override conditions
    elif (-0.1 <= polarity <= 0.1) or (result['score'] < 0.7):  # Lowered threshold
        return {
            'label': 'NEUTRAL',
            'score': max(0.7, 1 - abs(polarity))
        }
    return result

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        
        # Special case for truly neutral statements
        neutral_keywords = ['scheduled', 'meeting', 'temperature', 'time', 'located']
        if any(keyword in text.lower() for keyword in neutral_keywords):
            result = {'label': 'NEUTRAL', 'score': 0.95}
        else:
            result = analyze_sentiment(text)
            
        # Format label nicely
        sentiment = result["label"].capitalize()
        return render_template("result.html", 
                           text=text, 
                           sentiment=sentiment, 
                           confidence=result['score'])  # Pass raw float here
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)