from sentiment_analyzer import SentimentAnalyzer

def analyze_examples():
    analyzer = SentimentAnalyzer()
    examples = [
        "I absolutely love this new feature!",
        "The service was terrible and slow.",
        "Please schedule a meeting for next Tuesday",
        "I'm feeling okay about the decision",
        "The package will arrive at 3 PM"
    ]
    
    for text in examples:
        result = analyzer.analyze(text)
        print(f"Text: {text}")
        print(f"Sentiment: {result['label']} (confidence: {result['score']:.2f})")
        print("-" * 50)

if __name__ == '__main__':
    analyze_examples()