from functions import cointoss,rps,numguesser,wordle
def main():
    games[decision]()

print("Hello and welcome Lucas' arcade!")
run = True
games = {"rps":rps, "ht":cointoss, "ng":numguesser, "wd":wordle}
while run:
    decision = input("Please choose a game from the following:\nRock, Paper, Scissors(rps)\nCointoss(ht)\nNumber Guesser(ng)\nWordle(wd): ")
    if decision in games:
        main()
        run = False