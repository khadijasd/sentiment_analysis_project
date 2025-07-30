from transformers import pipeline
from textblob import TextBlob

class SentimentModels:
    def __init__(self):
        self._transformers_model = None
        self._textblob_model = TextBlob
    
    @property
    def transformers_model(self):
        if self._transformers_model is None:
            self._transformers_model = pipeline(
                "sentiment-analysis", 
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )
        return self._transformers_model
    
    @property
    def textblob_model(self):
        return self._textblob_model

models = SentimentModels()