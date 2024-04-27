from tools.increaseVocabulary import printDefinition, getDefinition, getRandomWord
import sys 
tools = [
'Increase Vocabulary'
]

def useTool():
    print("Enter a tool number: ")
    num = 1

    for tool in tools:
        print(f'{num}. {tool}')
    userChoice = input(": ")
    try:
        userChoice = int(userChoice)
    except ValueError:
        print("Invalid Choice")
        useTool()
    if userChoice == 1:
        word = getRandomWord()
        validOrNot, definition = getDefinition(word)
        printDefinition(word,validOrNot,definition)
    restartOrNot = input("Do you want to use another tool? (y/n): ").lower()
    if restartOrNot == 'y':
        useTool()
    else:
        sys.exit()
useTool()