import g4f

from test_promts import revenue, variable_production


def ask_gpt(promt):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.GeekGpt,
        messages=[{"role": "user", "content": promt}],
        stream=True,
    )
    return response


print(''.join(list(ask_gpt(revenue))))
