from openai import OpenAI
import json
from app.helpers.error import INTERNAL_SERVER_ERROR

client = OpenAI(
    api_key = userdata.get('openai_api_key')
)

class TextGenerationController:
    def __init__(self, api_key):
        pass

    async def generate_prompt(self, prompt, title, text):
        if text is None or (len(text)) < 100 or len(title) < 10:
            return prompt
        if len(prompt) > 88:
             prompt += ', '
        return f'{prompt}' + f'Título: {title}, Texto: {text}'


    def interact_with_AI (self, prompt, max_tokens=150):
        response = client.chat.completions.create(
            max_tokens=max_tokens,
            model="gpt-4o-mini",
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    async def execute(self, prompt, **article):
        for article in article_output:
            prompt = self.generate_prompt(prompt, **article)
    
        response = self.interact_with_AI(prompt)
        return response

prompt = 'Filter pertinent information and generate a summary in paragraph format in Brazilian Portuguese for the following news. Remember to consider all of them in the summary and that each news has the format "Title: " and "Text": '