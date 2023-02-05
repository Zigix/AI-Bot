from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')


def gpt_response(prompt):
    print(f'Prompt: {prompt}')
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=1,
        max_tokens=1000
    )
    response_choice = response.get('choices')
    print(f'Response: {response_choice}')
    if response_choice and len(response_choice) > 0:
        return response_choice[0]['text']
    return 'xd'
