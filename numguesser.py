# def numguess():
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
    if user == computer:
        ask = input(f"Congratulations, you have guessed the number out of {range} possibilities. Play again?(y/n): ")
        run = tf(ask)
    else:
        print("Keep trying.")
    if user == "quit":
        print("exiting...")
        run = False