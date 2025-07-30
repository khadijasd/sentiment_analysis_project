import unittest
from sentiment_analyzer.models import models

class TestModels(unittest.TestCase):
    def test_transformers_model_loading(self):
        model = models.transformers_model
        self.assertIsNotNone(model)
        
        # Test basic functionality
        result = model("I love this!")[0]
        self.assertIn(result['label'], ['POSITIVE', 'NEGATIVE'])
        self.assertIsInstance(result['score'], float)
    
    def test_textblob_model(self):
        blob = models.textblob_model("This is good")
        self.assertIsInstance(blob.sentiment.polarity, float)
        self.assertIsInstance(blob.sentiment.subjectivity, float)

if __name__ == '__main__':
    unittest.main()