import unittest
from sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SentimentAnalyzer()
    
    def test_positive_phrases(self):
        test_cases = [
            "I love this product!",
            "This is awesome!",
            "You're amazing!"
        ]
        for text in test_cases:
            result = self.analyzer.analyze(text)
            self.assertEqual(result['label'], 'POSITIVE')
            self.assertGreaterEqual(result['score'], 0.99)
    
    def test_neutral_keywords(self):
        test_cases = [
            "The meeting is scheduled for tomorrow",
            "Current temperature is 22 degrees",
            "The time is 3:45 PM"
        ]
        for text in test_cases:
            result = self.analyzer.analyze(text)
            self.assertEqual(result['label'], 'NEUTRAL')
    
    def test_negative_sentences(self):
        test_cases = [
            "I hate this!",
            "This is terrible",
            "The worst experience ever"
        ]
        for text in test_cases:
            result = self.analyzer.analyze(text)
            self.assertEqual(result['label'], 'NEGATIVE')
    
    def test_edge_cases(self):
        test_cases = [
            ("", {'label': 'NEUTRAL', 'score': 0.7}),  # Empty string
            ("12345", {'label': 'NEUTRAL', 'score': 0.7}),  # Numbers only
        ]
        for text, expected in test_cases:
            result = self.analyzer.analyze(text)
            self.assertEqual(result['label'], expected['label'])
            self.assertAlmostEqual(result['score'], expected['score'], places=1)

if __name__ == '__main__':
    unittest.main()