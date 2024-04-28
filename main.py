import tools.increaseVocabulary as increaseVocabulary
import tools.passwordGenerator as passwordGenerator
import sys 
tools = [
'Increase Vocabulary',
'Password Generator'
]

def useTool():
    print("Enter a tool number: ")
    num = 1
    for tool in tools:
        print(f'{num}. {tool}')
        num += 1
    userChoice = input(": ")
    try:
        userChoice = int(userChoice)
    except ValueError:
        print("Invalid Choice")
        useTool()
    if userChoice == 1:
        try:
            word = increaseVocabulary.getRandomWord()
            validOrNot, definition = increaseVocabulary.getDefinition(word)
            increaseVocabulary.printDefinition(word,validOrNot,definition)
        except Exception as e:
            print(f"Sorry!! There is some issue. Please try again. Error: {e}")
    elif userChoice == 2:
        try:
            lengthOfPassword = int(input("Enter length of password you want: "))
            passwordGenerator.getRandomPassword(length=lengthOfPassword)    
        except ValueError:
            print("Invalid length of password")
            useTool()
    restartOrNot = input("Do you want to use another tool? (y/n): ").lower()
    
    if restartOrNot == 'y':
        useTool()
    else:
        sys.exit()
useTool()