print("Hello and welcome Lucas' arcade!")
decision = input("Please choose from the following: Rock, Paper, Scissors(rps), Heads or Tails(ht): ")
if decision == "rps":
    from rps import rps
    rps()
if decision == "ht":
    from cointoss import cointoss
    cointoss()