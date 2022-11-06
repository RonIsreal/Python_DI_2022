'''Exercise 1: Temperature Advice

Create a function called get_random_temp().
This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
Test your function to make sure it generates expected results.

Create a function called main().
Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
between 16 and 23
between 24 and 32
between 32 and 40

Change the get_random_temp() function:
Add a parameter to the function, named ‘season’.
Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
Now that we’ve changed get_random_temp(), let’s change the main() function:
Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
Use the season as an argument when calling get_random_temp().

Bonus: Give the temperature as a floating-point number instead of an integer.
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
'''

import random

random.seed()

season = input("Please choose your preferred month (Spring, Summer, Autumn, Winter): ")
print(f"You have chosen {season.capitalize()}.")

def get_random_temp(season):
    if season.lower() == 'winter':
        rand_temp = float(random.randint(-10,10))
    elif season.lower() == 'autumn':
        rand_temp = float(random.randint(10,20))
    elif season.lower() == 'spring':
        rand_temp = float(random.randint(20,30))
    elif season.lower() == 'summer':
        rand_temp = float(random.randint(30,41))
    else:
        print('This is not a valid season. Please choose a valid season.')
        get_random_temp(season)
    return rand_temp


def main():
    random_temperature = get_random_temp(season)
    print(f"The temperature right now is {random_temperature} degrees Celsius.")
    if random_temperature < 0:
        print("Wow! So cold! Get dressed well!")
    elif random_temperature in range(0, 16):
        print(f"Chilly! You'll need a good coat!")
    elif random_temperature in range(16, 24):
        print(f"Not too cold, but also not too hot.")
    elif random_temperature in range(24, 32):
        print(f"A t-shirt is more than enough!")
    else:
        print("Hot! Beach time!")


main()

#Missing Bonus#2