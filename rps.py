def rps():
    import random
    from functions import tf, quit
    possact = ["r", "p", "s"]
    word_dict = {"r":"rock", "p":"paper", "s":"scissor"}    

    run = True
    while run:
        user = input("input rock(r), paper(p), or scissor(s): ")
        rand = random.choice(possact)
        run = quit(user)
        if rand == user:
            print("Same choice, try again")
        elif user == "r":
            if rand == "p":
                ask = str(input(f"computer won. you chose {word_dict.get(user)} and computer chose {word_dict.get(rand)}. Play again?(y/n): "))
                run = tf(ask)
            else:
                ask = str(input(f"you won. you chose {word_dict.get(user)} and computer chose {word_dict.get(rand)}. Play again?(y/n): "))
                run = tf(ask)
        elif user == "p":
            if rand == "s":
                ask = str(input(f"computer won. you chose {word_dict.get(user)} and computer chose {word_dict.get(rand)}. Play again?(y/n): "))
                run = tf(ask)
            else:
                ask = str(input(f"you won. you chose {word_dict.get(user)} and computer chose {word_dict.get(rand)}. Play again?(y/n): "))
                run = tf(ask)
        elif user == "s":
            if rand == "r":
                ask = str(input(f"computer won. you chose {word_dict.get(user)} and computer chose {word_dict.get(rand)}. Play again?(y/n): "))
                run = tf(ask)
            else:
                ask = str(input(f"you won. you chose {word_dict.get(user)} and computer chose {word_dict.get(rand)}. Play again?(y/n): "))
                run = tf(ask)