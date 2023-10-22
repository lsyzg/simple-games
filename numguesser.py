def numguesser():
    import random
    run = True
    range = int(input("What would you like the range to be?: "))
    computer = random.randint(1,range)
    def tf(ask):
            if ask == "n":
                print("exiting...")
                return False
            else:
                return True
    while run:
        user = input("What number do you think it is?: ")
        if user.isnumeric():
            user = int(user)
            if user == computer:
                ask = input(f"Congratulations, you have guessed the number out of {range} possibilities. Play again?(y/n): ")
                run = tf(ask)
                if run == True:
                    range = int(input("What would you like the range to be?: "))
                    computer = random.randint(1,range)       
            else:
                print("Keep trying.")
        else:
            if user == "quit":
                print(f"the number was {computer}.")
                print("exiting...")
                run = False