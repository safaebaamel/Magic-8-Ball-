import time
import random
import sys

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ #B')
print('')

answers = ["Yes!", "No way Man!, are you serious!", "I think so", "Are you sure ? this may chock you! Ask alter.", "NO; Sorryy ..", "Hell yeah", "probably not","Of course yes"]

def giveanswers():
    question = input("Here, you get to ask the master of 8-Balls game a question. ")
    if question == "":
        sys.exit()
    print("Emm, wait a little bit")
    time.sleep(2)
    print("It is coming ..")
    time.sleep(1)
    print("Here we go :P!")
    print(">>>>>>>>>>" + random.choice(answers) + "<<<<<<<<<<")

giveanswers()
