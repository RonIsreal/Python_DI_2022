import random

random.seed()

def StartGame():
    colors = ('red','orange','purple','pink','blue','yellow','violet','green','gray')
    random_color = random.choice(colors)
    try_counter = 1
    print(f" Try {try_counter} out of 6.")
    while True:
        user_guess = input("Guess which color is the right one: ")
        if try_counter == 6:
            print("Busted, out of tries!")
            break
        elif user_guess.lower() != random_color:
            try_counter += 1
            print(f" Try {try_counter} out of 6.")
        else:
            print("You got it!")
            break

StartGame()