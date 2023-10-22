def cointoss():
    import random

    ht = ["heads","tails"]
    head_tails = random.choice(ht)
    if input("Heads or tails? (lowercase): ") == head_tails:
        print(f"You win! Computer chose {head_tails}")
    else:
        print(f"You lost. Computer chose {head_tails}")