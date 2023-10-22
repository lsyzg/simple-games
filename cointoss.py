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
        if input("Heads or tails?: ") == head_tails:
            yn = input(f"You win! Computer chose {ht_dict.get(head_tails)}. Play again?(y/n): ")
            run = tf(yn)
        else:
            yn = input(f"You lost. Computer chose {ht_dict.get(head_tails)}. Play again?(y/n): ")
            run = tf(yn)