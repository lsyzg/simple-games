print("Hello and welcome Lucas' arcade!")
decision = input("Please choose from the following: Rock, Paper, Scissors(rps), Cointoss(ht), or Number Guesser(ng): ")

if decision == "rps":
    from rps import rps
    rps()
if decision == "ht":
    from cointoss import cointoss
    cointoss()
if decision == "ng":
    from numguesser import numguesser
    numguesser()
