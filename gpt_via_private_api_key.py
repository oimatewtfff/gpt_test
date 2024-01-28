import environ
import openai

env = environ.Env()
environ.Env.read_env()
openai.api_key = env("API_KEY")


def ask_gpt(promt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt}],
        stream=True,
    )
    return response
