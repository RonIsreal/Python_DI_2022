'''Exercise 1:

Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
Call the function, and make sure the message displays correctly.
'''

def display_message():
    print("I am learning Python!")

display_message()

'''Exercise 2:

Write a function called favorite_book() that accepts one parameter called title.
The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
Call the function, make sure to include a book title as an argument when calling the function.
'''

def favorite_book(title):
    print(f"One of my favorite books is '{title}'.")

favorite_book("The Catcher in the Rye")

'''Exercise 3:

Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as “Reykjavik is in Iceland”.
Give the country parameter a default value.
Call your function.
'''

def describe_city(city, country = 'Brazil'):
    print(f"{city.capitalize()} is in {country.capitalize()}.")
    
describe_city('sao paulo')

'''Exercise 4:

Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
'''
import random
random.seed()


def compare_numbers(num1, num2 = random.randint(1, 100)):
    if num1 == num2:
        print("Congrats! Your chosen number matches my random number!")
    else:
        print(f"Oh too bad! Your number {num1} doesn't match my number {num2}.")

compare_numbers(20)

'''Exercise 5:

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function make_shirt() using positional arguments to make a shirt.
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
Bonus: Call the function make_shirt() using keyword arguments.
'''

def make_shirt(size = 'L', text = 'I love Python!'):
    print(f"Your size {size} t-shirt will be made with the following message: '{text}'")

make_shirt()
make_shirt('L')
make_shirt('M')
make_shirt(text = "Booyah!")

'''Exercise 6:

Make a list of magician’s names.
Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
Call the function make_great().
Call the funcyion show_magicians() to see that the list has actually been modified.
'''

magicians = ['Saruman', 'Gandalf', 'Merlin']

def show_magicians():
    for magician in magicians:
        print(magician)

def make_great():
    for magician in magicians:
        magician = magician + " the Great"
        print(magician)

make_great()
show_magicians()
    
    

    




