import openai
import os


def call_chatgpt3(api_key, prompt, max_tokens):

    openai.api_key = api_key

    # Generate text using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
    )

    return response.choices[0].text

