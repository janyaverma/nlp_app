import nlpcloud

class API:

    def __init__(self):
        self.client = nlpcloud.Client("gpt-oss-120b", "INSERT-YOUR-API-KEY-HERE", gpu=True)

    def sentiment_analysis(self,text):
        response = self.client.sentiment(text, target="NLP Cloud")
        return response
    
    def ner(self,text,search_term):
        response = self.client.entities(text,searched_entity=search_term)
        return response
    
    def intent_analysis(self,text):
        response = self.client.intent_classification(text)
        return response