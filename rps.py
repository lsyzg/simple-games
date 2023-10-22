def rps():
    import random
    possact = ["rock", "paper", "scissor"]

    run = True
    while run:
        user = input("input rock, paper, or scissor: ")
        rand = random.choice(possact)
        print(f"computer chose {rand}")
        if rand == user:
            print("Same choice, try again")
        elif user == "rock":
            if rand == "paper":
                print(f"computer won. you chose {user} and computer chose {rand}")
                run = False
            else:
                print(f"you won. you chose {user} and computer chose {rand}")
                run = False
        elif user == "paper":
            if rand == "scissor":
                print(f"computer won. you chose {user} and computer chose {rand}")
                run = False
            else:
                print(f"you won. you chose {user} and computer chose {rand}")
                run = False
        elif user == "scissor":
            if rand == "rock":
                print(f"computer won. you chose {user} and computer chose {rand}")
                run = False
            else:
                print(f"you won. you chose {user} and computer chose {rand}")
            run = False