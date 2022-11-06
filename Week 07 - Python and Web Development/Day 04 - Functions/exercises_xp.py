'''Exercise 1:

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
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.'''

import random

random.seed()


def get_random_temp():
    month = int(input("Please choose between the 12 months (1 for January, 2 for February, etc: "))
    season = ''
    if month in range(3, 6):
        temp = float(random.randint(25, 31))
        season = "Spring"
    elif month in range(6, 9):
        temp = random.randint(31, 41)
        season = "Summer"
    elif month in range(9, 12):
        temp = random.randint(17, 25)
        season = "Autumn"
    elif month >= 13:
        print("Not a valid month.")
    else:
        temp = random.randint(-10, 17)
        season = "Winter"
    return float(temp)


def main():
    current_temp = get_random_temp()
    if current_temp < 0:
        print(f"The temperature right now is {current_temp}º Celsius. Wear warm clothes!")
    elif current_temp in range(0, 17):
        print(f"The temperature right now is {current_temp}º Celsius. Chilly!")
    elif current_temp in range(17, 24):
        print(f"The temperature right now is {current_temp}º Celsius. A bit cold but all good.")
    elif current_temp in range(24, 33):
        print(f"The temperature right now is {current_temp}º Celsius. Warm and nice!")
    else:
        print(f"The temperature right now is {current_temp}º Celsius. Hawt!")


main()

'''Exercise 2: When Will I Retire ?
Instructions
The point of the exercise is to check if a person can retire depending on their age and their gender.
Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

Create a function get_age(year, month, day)
Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
After calculating the age of a person, the function should return the age (the age is an integer).
Create a function can_retire(gender, date_of_birth).
It should call the get_age function (with what arguments?) in order to receive an age.
Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
Calculate. You may need to do a little more hard-coding here.
Return True if the person can retire, and False if he/she can’t.
Some Hints

Ask for the user’s gender as “m” or “f”.
Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
Call can_retire to get a definite value for whether the person can or can’t retire.
Display a message informing the user whether they can retire or not.
As always, test your code to ensure it works.'''

from datetime import date


def get_age(bdate):
    y, m, d = bdate.split(',')
    y = y.lstrip('0')
    m = m.lstrip('0')
    d = d.lstrip('0')
    today = date.today()
    return (
        today.year - int(y) - ((today.month, today.day) < (int(m), int(d)))
    )



def can_retire():
    bdate = input('Please input your date of birth in the following format "YYYY,MM,DD": ')
    user_gender = input('Please inform your gender by using "M" for Male or "F" for Female: ')
    user_age = get_age(bdate)
    if user_gender.lower() == 'm' and user_age < 67:
        print("You are ineligible for retirement. The minimum retirement age for men is 67 years old.")
    elif user_gender.lower() == 'm' and user_age >= 67:
        print("You are eligible for retirement.")
    elif user_gender.lower() == 'f' and user_age < 62:
        print("You are ineligible for retirement. The minimum retirement age for women is 62 years old.")
    elif user_gender.lower() == 'f' and user_age >= 62:
        print("You are eligible for retirement.")
    else:
        print("The information you provided is invalid.")


print(can_retire())

'''Exercise 3:
Instructions
Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
Example:

If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)'''

def digit_sum(x):
    lst = [str(x)*i for i in range(1,5)]
    equation = "+".join(lst)
    result = sum(map(int, lst))
    print(f"{equation} = {result}")

digit_sum(3)
