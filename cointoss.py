def cointoss():
    import random
    from functions import tf, quit
    ht = ["h","t"]
    ht_dict = {"h":"heads","t":"tails"}
    run = True
    while run:
        head_tails = random.choice(ht)
        user = input("Heads(h) or tails(t)?: ")
        run = quit(user)
        if user == head_tails:
            ask = input(f"You win! The coin flipped {ht_dict.get(head_tails)}. Play again?(y/n): ")
            run = tf(ask)
        else:
            ask = input(f"You lost. The coin flipped {ht_dict.get(head_tails)}. Play again?(y/n): ")
            run = tf(ask)