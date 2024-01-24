def pig():
    import random
    bot_score = 0
    user_score = 0
    temp_score = 0
    run = True
    run1 = True
    goal_score = int(input("what do you want the winning threshold to be? (number): "))
    def roll():
        roll = random.randint(1,6)
        return roll

    while run:
        while run1:
            cont = input("would you like to roll? (y/n): ")
            if cont == "y":
                indiv_roll = roll()
                print(indiv_roll)
                if indiv_roll == 1:
                    print("Sorry, you rolled a one and lost all your points from this turn")
                    temp_score = 0
                    run1 = False
                    run2 = True
                else:
                    temp_score += indiv_roll
            elif cont == "n":
                user_score += temp_score
                temp_score = 0
                print(f"your score is: {user_score}")
                if user_score >= goal_score:
                    print("you win!")
                    run2 = False
                    run = False
                    break
                run1 = False
                run2 = True
            else:
                print(f"please say y or n instead of {cont}")
                continue
        while run2:
            bot_iterations = random.randint(1,10)
            for bot_roll in range(bot_iterations):
                bot_roll = roll()
                if bot_roll == 1:
                    temp_score = 0
                    run1 = True
                    run2 = False
                else:
                    temp_score += bot_roll
            bot_score += temp_score
            temp_score = 0
            print(f"the robot's score is: {bot_score}")
            if bot_score >= goal_score:
                    print("robot wins")
                    run = False
                    break
            run1 = True
            run2 = False