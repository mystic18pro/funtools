import requests
from tools.APIKEY import apiKey



def getRandomPassword(length: int) -> str:
    api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
    randPassword = requests.get(api_url, headers={'X-Api-Key': apiKey}).json()
    print("Your password: ",randPassword)

