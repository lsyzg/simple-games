# to call a function say: from functions import [function you want to use, example: tf, quit etc.]
from cointoss import cointoss
from numguesser import numguesser
from rps import rps
from wordle import wordle

def tf(ask):
    if ask == "n":
        print("exiting...")
        return False
    else:
        return True

def quit(user): 
    if user == "quit":
        print("exiting...")
        return False
    else:
        return True