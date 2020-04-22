import time
import random 
import sys

#sys : This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

inp = "Ask the Magic 8-Ball a question (Return or enter to quit) "

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')

while 1:
    question = input(inp)
    answer = random.randint(1,8)
    time.sleep(2)

    if question == "":
        sys.exit()
    elif answer == 1:
        print("Maybe Yes")
        break
    elif answer == 2:
        print("Absolutely No")
        break
    elif answer == 3:
        print("Ask again later, I'm not so sure about it")
        break
    elif answer == 4:
        print("How dare you Ask, you know deep in your heart that it is true")
        break
    elif answer == 5:
        print("Not really .. sorry!")
        break
    elif answer == 6:
        print("Things may change in your life if you knew the answer, are you sure you wanna know ?! Ask later")
        break
    elif answer == 7:
        print("I say NO")
        break
    elif answer == 8:
        print("No way! duuude!")
        break

