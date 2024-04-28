import requests
from tools.APIKEY import apiKey

randWordsURL = 'https://api.api-ninjas.com/v1/randomword'
def getRandomWord() -> str:
    randWordsResponse = requests.get(randWordsURL, headers={'X-Api-Key': apiKey})

    return randWordsResponse.json()['word']


def getDefinition(word:str) -> str:

    definitionURL = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
    definitionResponse = requests.get(definitionURL, headers={'X-Api-Key': apiKey})

    validOrNot = definitionResponse.json()['valid']
    definition = definitionResponse.json()['definition']
    return validOrNot,definition



# Printing part
def printDefinition(word:str,validOrNot:str,definition:str) -> None:
    if validOrNot == True:
        print(f"Increase your vocabulary!!\nWord: {word}\nDefinition: {definition}")
    else: 
        print(f"Sorry!! There is some issue. Please try again.")


