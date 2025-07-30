from sentiment_analyzer import SentimentAnalyzer

def analyze_phrase():
    analyzer = SentimentAnalyzer()
    print("Sentiment Analysis Console (type 'quit' to exit)")
    while True:
        text = input("\nEnter a phrase: ")
        if text.lower() == 'quit':
            break
        result = analyzer.analyze(text)
        print(f"Result: {result['label']} (confidence: {result['score']:.2f})")

if __name__ == "__main__":
    analyze_phrase()