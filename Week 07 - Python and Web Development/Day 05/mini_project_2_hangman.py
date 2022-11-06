import random


def welcome():
    logo = """
    __  _____    _   __________  ______    _   __
   / / / /   |  / | / / ____/  |/  /   |  / | / /
  / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ / 
 / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /  
/_/ /_/_/  |_/_/ |_/\____/_/  /_/_/  |_/_/ |_/  """
    print(logo)
    print('WELCOME!')
    user_name = input('What is your name? ')
    print(f'Have fun {user_name}!')
    print('You have 6 tries.')


def choose_word():
    fruits = ['Apple', 'Banana', 'Blackberry', 'Blueberry', 'Cherry', 'Coconut', 'Cranberry', 'Date', 'Grape', 'Raisin',
              'Grapefruit', 'Kiwi', 'Lemon', 'Lime', 'Mango', 'Melon', 'Cantaloupe', 'Watermelon', 'Orange',
              'Clementine', 'Tangerine', 'Papaya', 'Peach', 'Pear', 'Plum', 'Prune', 'Pineapple', 'Pomegranate',
              'Raspberry']
    secret_word = random.choice(fruits)
    secret_word = secret_word.lower()
    print("Are you ready?......let's play!")
    print('hint! its a fruit!')
    return secret_word


welcome()


def game():
    word = choose_word()
    guesses = " "
    tries = 6

    while tries > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            tries = -1
            choice = input("Would you like to play again? y/n\n")
            if "y" in choice:
                word = choose_word()
                guesses = " "
                tries = 5
            elif "n" in choice:
                print('bye!')
                exit()
        guess = input("Guess a character:")
        guesses += guess
        if guess not in word:
            tries -= 1
            print("Wrong!")
            print(f"You have {tries} more guesses.")
            if tries == 0:
                print("You lost!")
                h1 = """ 
--------
|       |
|       0
|      /|\
|      / \
-------      """
                print(h1)
                choice = input("Would you like to play again? y/n\n")
                if "y" in choice:
                    word = choose_word()
                    guesses = " "
                    tries = 5
                elif "n" in choice:
                    print('bye!')
                    exit()
            if tries == 5:
                        h1 = """ 
            --------
            |       |
            |       0
            |      
            |      
            -------
                            """
            if tries == 4:
                h1 = """ 
--------
|       |
|       0
|      
|      
-------
                """
                print(h1)
            elif tries == 3:
                h1 = """ 
--------
|       |
|       0
|      /|
|      
-------
                  """
                print(h1)
            elif tries == 2:
                h1 = """ 
--------
|       |
|       0
|      /|\
|      
-------
                """
                print(h1)
            elif tries == 1:
                h1 = """ 
--------
|       |
|       0
|      /|\
|      / 
-------
                """
                print(h1)


choice1 = input("Would you like to play :) ? y/n\n")
if "y" in choice1:
    game()
