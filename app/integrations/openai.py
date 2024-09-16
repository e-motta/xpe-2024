from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

from app.config import OpenAIMessages


client = OpenAI()


def generate_chat_completion(messages: OpenAIMessages) -> ChatCompletion:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return completion
