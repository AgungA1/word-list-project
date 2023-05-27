import requests

api_key = 'c5540619-4f6f-4cb1-952b-9ee30c4c9f6f'
word = 'impulse'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)