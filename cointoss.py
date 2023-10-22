def cointoss():
    import random
    def tf(yn):
        if yn == "n":
            print("exiting...")
            return False
        else:
            return True
    ht = ["h","t"]
    ht_dict = {"h":"heads","t":"tails"}
    run = True
    while run:
        head_tails = random.choice(ht)
        user = input("Heads(h) or tails(t)?: ")
        if user == head_tails:
            ask = input(f"You win! The coin flipped {ht_dict.get(head_tails)}. Play again?(y/n): ")
            run = tf(ask)
        else:
            ask = input(f"You lost. The coin flipped {ht_dict.get(head_tails)}. Play again?(y/n): ")
            run = tf(ask)