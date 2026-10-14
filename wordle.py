import requests
import json
from colorama import Fore,Style,Back


URL = "https://wordlehints.co.uk/wp-json/wordlehint/v1/answers/latest"
rawrequest = requests.get(url=URL)
isguessing = True
x=0
whatwasright = f""

full = json.loads(rawrequest.content)

# the result is a Python dictionary:
answer = (full["answer"])

def guess():
    global isguessing
    while isguessing:
        guess = input("what is your guess?\n> ").upper()
        if len(guess) > 5:
            print("guess is too long! make sure it is 5 letters")
            continue
        else:
            isguessing = False
            checkguess(guess)
            
def checkguess(guess):
    global x,whatwasright
    for i in guess:
        if (i != answer[x]) and (i in answer):
            whatwasright += f"{Back.YELLOW}{i}{Style.RESET_ALL}" 
        elif i == answer[x]:
            whatwasright += f"{Back.GREEN}{i}{Style.RESET_ALL}"
        else:
            whatwasright += f"{Back.BLACK}{i}{Style.RESET_ALL}"
        checkifwon(guess,answer)
        x+=1
        
def checkifwon(guess,answer):
    if guess == answer:
        print(f"correct! the answer was {answer}!")
        quit()
        
guess()
print(whatwasright)
