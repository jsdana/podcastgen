import openai
import os
from app.controllers.post_extract_controller import TextGenerationController
from app.infrastructure.repositories.mongo_extract_repository import TextRepository

openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key is None:
    raise ValueError("API key not found. Make sure the OPENAI_API_KEY environment variable is set.")

openai.api_key = openai_api_key
class GenerateFormUseCase:

    def __init__(self, text_repository: TextRepository):
        self.text_repository = text_repository
        self.process_generated_text = TextGenerationController(api_key=openai_api_key)
    
    async def process_generated_text(self, generated_text: str):
        pass
