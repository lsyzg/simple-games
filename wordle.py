def wordle(): 
    import pathlib
    import random
    from functions import tf,quit

    run = True
    correct = []
    misplaced = {}
    wrong = {}
    availablelets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    tries = 0
    words = pathlib.Path("valid-wordle-words.txt")
    wordlist = [
        word.lower()
        for word in words.read_text(encoding="utf-8").strip().split("\n")
    ]
    word = random.choice(wordlist)

    while run:
        user = input("Guess a word that is five letters long: ")
        if len(user) == 5 or user == "quit":
            if tries == 6:
                ask = input(f"Oops, you ran out of tries. The word was {word}. Play again? (y/n)")
                run = tf(ask)
            run = quit(user)
            if user == word:
                ask = (f"Correct, you have guessed it after {tries} tries. Play again? (y/n)")
                run = tf(ask)
            else:
                for a_letter, b_letter in zip(user, word):
                    if a_letter == b_letter:
                        correct.append(a_letter)
                correctlet = set(correct)
                misplaced = set(word).intersection(set(user)) - correctlet
                wrong = set(user) - set(word)
                availablelets = availablelets - wrong

                print("You got these letters in the correct place: " + ', '.join(correctlet))
                print("You got these letters in the wrong place: " + ', '.join(misplaced))
                print("The letters are not in the word: " + ', '.join(wrong))
                print("You can still use these letters: " + ', '.join(availablelets))
                tries += 1
        elif user != "quit" and len(user) > 5 or len(user) < 5:
            print("Use a word that is five letters long, no more no less")