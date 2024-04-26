import requests
from tools.APIKEY import apiKey

randWordsURL = 'https://api.api-ninjas.com/v1/randomword'
randWordsResponse = requests.get(randWordsURL, headers={'X-Api-Key': apiKey})

word = randWordsResponse.json()['word']

definitionURL = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
definitionResponse = requests.get(definitionURL, headers={'X-Api-Key': apiKey})

validOrNot = definitionResponse.json()['valid']
definition = definitionResponse.json()['definition']


# Printing part
def randomDefinition():
    if validOrNot == True:
        print(f"Increase your vocabulary!!\nWord: {word}\nDefinition: {definition}")
    else: 
        print(f"Sorry!! There is some issue. Please try again.")
        randomDefinition(word, validOrNot, definition)


