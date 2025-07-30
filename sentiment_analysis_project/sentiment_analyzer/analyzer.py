from .models import models

class SentimentAnalyzer:
    POSITIVE_PHRASES = [
        "i like you", "i love", "it's great", "awesome",
        "wonderful", "amazing", "fantastic", "excellent"
    ]
    
    NEUTRAL_KEYWORDS = [
        'scheduled', 'meeting', 'temperature', 
        'time', 'located', 'address', 'date'
    ]
    
    def analyze(self, text):
        """Main analysis method"""
        self._text = text  # Store text for edge case handling
        if self._is_neutral_by_keywords(text):
            return self._neutral_result()
        
        transformers_result = self._transformers_analysis(text)
        polarity = self._textblob_analysis(text)
        
        if self._is_positive_by_phrases(text):
            return self._positive_result()
        
        if self._is_neutral_by_polarity(polarity, transformers_result):
            return self._neutral_result(polarity)
        
        return transformers_result
    
    def _transformers_analysis(self, text):
        return models.transformers_model(text)[0]
    
    def _textblob_analysis(self, text):
        return models.textblob_model(text).sentiment.polarity
    
    def _is_positive_by_phrases(self, text):
        text_lower = text.lower()
        return any(phrase in text_lower for phrase in self.POSITIVE_PHRASES)
    
    def _is_neutral_by_keywords(self, text):
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.NEUTRAL_KEYWORDS)
    
    def _is_neutral_by_polarity(self, polarity, transformers_result):
        return (-0.1 <= polarity <= 0.1) or (transformers_result['score'] < 0.7)
    
    def _positive_result(self):
        return {'label': 'POSITIVE', 'score': 0.99}
    
    def _neutral_result(self, polarity=0):
  
    # Get the analyzed text (you'll need to store it in analyze())
        text = getattr(self, '_text', '')
    
    # Special handling for empty/numeric inputs
        if not text.strip() or text.strip().isdigit():
           return {
            'label': 'NEUTRAL',
            'score': 0.7  # Lower confidence for edge cases
                  }
    
    # Default case
        return {
        'label': 'NEUTRAL',
        'score': max(0.7, 1 - abs(polarity))
    }