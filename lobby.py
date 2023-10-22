print("Hello and welcome Lucas' arcade!")
decision = input("Please choose a game from the following:\nRock, Paper, Scissors(rps)\nCointoss(ht)\nNumber Guesser(ng): ")

if decision == "rps":
    from rps import rps
    rps()
if decision == "ht":
    from cointoss import cointoss
    cointoss()
if decision == "ng":
    from numguesser import numguesser
    numguesser()