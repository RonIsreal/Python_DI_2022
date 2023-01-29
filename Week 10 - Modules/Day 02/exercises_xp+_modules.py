'''🌟 Exercise 2: Random Module
Instructions
Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
if it’s the same number, display a success message to the user, else don’t.'''
import datetime
import random
import string
import datetime as dt
from datetime import date
from faker import Faker
def sameNumber():
    user_number = input("Please choose a number between 1 and 100: ")
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Same number! Lucky!")
    else:
        print(f"Not this time. The correct number was {random_number}.")


# sameNumber()

'''Exercise 3: String Module
Instructions
Generate random String of length 5
Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
Hint: use the string module'''

random_letters = list(string.ascii_letters)


def generateString():
    gen_str = "".join(random.choice(random_letters) for i in range(5))
    print(gen_str)


generateString()

'''🌟 Exercise 4 : Current Date
Instructions
Create a function that displays the current date.
Hint : Use the datetime module'''


def currentDate():
    date_now = datetime.date.today().strftime('%d/%m/%Y')
    print(f"Today's date: {date_now}.")


currentDate()

'''Exercise 5 : Amount Of Time Left Until January 1st
Instructions
Create a function that displays the amount of time left from now until January 1st.
(Example: the 1st of January is in 10 days and 10:34:01hours).'''


def days_left_in_year():
    day_of_year = datetime.date.today().timetuple().tm_yday
    days_left = 365 - day_of_year
    print(days_left)


def days_left_delta():
    today_date = datetime.date.today()
    january1st = datetime.date(2023, 1, 1)
    days_left = today_date - january1st
    print(days_left)


days_left_in_year()
days_left_delta()

'''Exercise 6 : Birthday And Minutes
Instructions
Create a function that accepts a birthdate as an argument (in the format of your choice), 
then displays a message stating how many minutes the user lived in his life.'''


# timedeltas calculate difference between two dates

def set_birthdate():

    today_date = datetime.date.today()
    bday = int(input("Please write the day of your birthday: "))
    bmonth = int(input("Please write the year of your birthday: "))
    byear = int(input("Please write which year you were born: "))
    bdate = datetime.date(byear, bmonth, bday)

    days_lived = today_date - bdate
    minutes_lived = days_lived.days * 1440
    print(f"You have lived {minutes_lived} minutes in your life so far!")


set_birthdate()

'''Exercise 7 : Upcoming Holiday
Instructions
Write a function that displays today’s date.
The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
Hint: Start by hardcoding the datetime and name of the upcoming holiday.'''

def todayandholiday():

    today_date = datetime.date.today()
    new_year = datetime.date(2022,12,31)
    days_left = new_year - today_date
    print(f"Today is {today_date.strftime('%d/%m/%Y')}. The next holiday will be in {days_left} (New Year's).")

todayandholiday()

'''Exercise 8 : How Old Are You On Jupiter?
Instructions
Given an age in seconds, calculate how old someone would be on:
Earth: orbital period 365.25 Earth days, or 31557600 seconds
Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years
So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.'''


def my_age():
    global my_age_seconds
    my_age = int(input("How old are you?: "))
    my_age_seconds = my_age * 31557600
    print(f"I am {my_age} years old on Earth. Or {my_age_seconds} seconds old!")


def my_age_mercury():
    age_seconds_mercury = my_age_seconds / 0.2408467
    print(f"In Mercury I am {age_seconds_mercury} seconds old!")


def my_age_venus():
    age_seconds_venus = my_age_seconds / 0.61519726
    print(f"In Venus I am {age_seconds_venus} seconds old!")


def my_age_mars():
    age_seconds_mars = my_age_seconds / 1.8808158
    print(f"In Mars I am {age_seconds_mars} seconds old!")


def my_age_jupiter():
    age_seconds_jupiter = my_age_seconds / 11.862615
    print(f"In Jupiter I am {age_seconds_jupiter} seconds old!")


def my_age_saturn():
    age_seconds_saturn = my_age_seconds / 29.447498
    print(f"In Saturn I am {age_seconds_saturn} seconds old!")


def my_age_uranus():
    age_seconds_uranus = my_age_seconds / 84.016846
    print(f"In Uranus I am {age_seconds_uranus} seconds old!")


def my_age_neptune():
    age_seconds_neptune = my_age_seconds / 164.79132
    print(f"In Neptune I am {age_seconds_neptune} seconds old!")


def doall():
    my_age()
    my_age_mercury()
    my_age_venus()
    my_age_mars()
    my_age_jupiter()
    my_age_saturn()
    my_age_uranus()
    my_age_neptune()


doall()

'''Exercise 9 : Faker Module
Instructions
Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
Create an empty list called users. Tip: It should be a list of dictionaries.
Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.'''

fk = Faker() #creates an instance of the faker module

users = []

def addUser(user_quant):
    while len(users) < user_quant:

        user_dict = dict({'name': fk.name(), 'address': fk.address(), 'language_code': fk.locale()})
        users.append(user_dict)
    return

addUser(2)
print(users)











