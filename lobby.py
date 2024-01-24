from functions import cointoss,rps,numguesser,wordle,pig
def main():
    games[decision]()

print("Hello and welcome Lucas' arcade!")
run = True
games = {"rps":rps, "ht":cointoss, "ng":numguesser, "wd":wordle, "p":pig}
while run:
    decision = input("Please choose a game from the following:\nRock, Paper, Scissors(rps)\nCointoss(ht)\nNumber Guesser(ng)\nWordle(wd)\nPig(p): ")
    if decision in games:
        main()
        run = False