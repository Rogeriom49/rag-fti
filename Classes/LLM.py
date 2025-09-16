from crewai import LLM
from langchain_google_genai import ChatGoogleGenerativeAI
class LLMCreator:
    def __init__(self, model, key):
        self.model = model
        self.key = key
    def create(self):
        return LLM(model=self.model, api_key=self.key, temperature=0.0)
    
    def create_gemini(self):
        model = ChatGoogleGenerativeAI(model=self.model, api_key=self.key, temperature=0.0)
        return model 