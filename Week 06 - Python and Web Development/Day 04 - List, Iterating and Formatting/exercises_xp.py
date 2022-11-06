'''Exercise 1:

Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
'''

my_fav_numbers = set()
my_fav_numbers.add(1)
my_fav_numbers.add(8)
my_fav_numbers.remove(1)
friend_fav_numbers = set()
friend_fav_numbers.add(2)
friend_fav_numbers.add(5)
our_fav_numbers = set.union(my_fav_numbers, friend_fav_numbers)

'''Exercise 2:

Given a tuple which value is integers, is it possible to add more integers to the tuple?
'''

# You can't add more integers to the tuple because tuples are immutable.
# One of the ways to do so is by converting the tuple into a list, adding the number into this list,
# and then converting the list back into a tuple.

my_tuple = (1, 2, 3)
tuple_list = list(my_tuple)
tuple_list.append(4)
my_tuple = tuple(tuple_list)
print(my_tuple)

'''Exercise 3:

Use a for loop to print all numbers from 1 to 20, inclusive.
'''

numbers = range(1,21) #last number is 21 because in ranges the last number is not inclusive. So the range ends one number before
for number in numbers:
	print(number)
	
'''Exercise 4:

Recap – What is a float? What is the difference between an integer and a float? A: Float is a number with decimals while integers are only whole numbers.
Can you think of another way to generate a sequence of floats? A: Although floats can't be sequenced like integers, you can use Numpy module to sequence them.
Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
'''

import numpy as np

start = 1.5
stop = 5.5
step = 0.5
float_range_list = list(np.arange(start, stop, step))
print(float_range_list)

'''Exercise 5:

Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
'''

basket = ["banana", "apples", "oranges", "blueberries"]
basket.remove("banana")
basket.remove("blueberries")
basket.append("kiwi")
basket.insert(0, "apples")
apple_count = basket.count("apples")
print(apple_count)
print(basket)
basket.clear()
print(basket)

'''Exercise 6:

Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
'''

real_name = 'ronny'
while True:
	name = input("Please write a name: ")
	if name.lower() == real_name:
		print("Congrats!")
		break
	else:
		print("Wrong name! Try again!")

'''Exercise 7:

Given a list, use a loop to print out every element which has an even index.
'''

count = range(1, int(input("Please enter a number: "))+1) #The number input will determine the range
for i in count:
	if count.index(i) % 2 == 0:
		print(i)

# Or if we want to print the numbers that are even within the range

for i in count:
	if i % 2 == 0:
		print(i)
		
'''Exercise 8:

Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
'''

# Print all numbers that are multiples of 5 or 7

for number in range(1500,2501):
  if number % 5 == 0 or number % 7 == 0:
    print(number)

# Print all numbers that are multiples of 5 AND 7
print("_______________________________________")


for number in range(1500,2501):
  if number % 5 == 0 and number % 7 == 0:
    print(number)

'''Exercise 9:

Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
'''

fruits = input("Please enter all the fruits you like separated by comma. ")
fruit_list = list(fruits.split(",").lower())
print(fruit_list)
while True:
	what_fruit = input("Which fruit are you craving right now? ")
	if what_fruit.lower() not in fruit_list:
		print("You chose a new fruit. Hope you enjoy!")
		break
	else:
		print("You chose one of your favourites. Enjoy!")
		break

'''Exercise 10:

Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
'''

pizza = []
while True:
	toppings = input("Please add each topping at a time and when finished write 'quit': ")
	if toppings.lower() != 'quit':
		print(f"{toppings} was added to your pizza.")
		pizza.append(toppings)
	else:
		pizza_total = 10 + (len(pizza) * 2.5)
		print(f"You have added {pizza} to your pizza.\n Your total price will be ${pizza_total}")
		break

'''Exercise 11:

A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.
Ask a family the age of each person who wants a ticket.
Store the total cost of all the family’s tickets and print it out.
A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.
'''

total_price = 0
age = " "
while age:
	age = input("How old are you? ")
	if not age:
		break
	elif int(age) in range(0,3):
		pass
	elif int(age) in range(3,13):
		total_price += 10
	else:
		total_price += 15
print(f"Your total price will be ${total_price}")

'''Exercise 12:

Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
At the end, print the final list.
'''

users = ['joe', 'jane', 'jeff', 'jenn']
for user in reversed(users):
	age = input(f"How old are you, {user}?")
	if int(age) < 16:
		users.remove(user)
	else:
		continue
print(users)

'''Exercise 13:

Make a list called sandwich_orders and fill it with the names of various sandwiches .
Then make an empty list called finished_sandwiches.
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
'''

sandwich_orders = ['cheeseburger', 'hamburger', 'cheesebacon']
finished_sandwiches = []
for sandwich in sandwich_orders:
	finished_sandwiches.append(sandwich)
for sandwich_ready in finished_sandwiches:
	print(f"I made your {sandwich_ready}")

'''Exercise 14:

Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches.
'''

sandwich_orders = ['cheeseburger', 'hamburger', 'cheesebacon', 'pastrami', 'pastrami', 'pastrami']
print("The deli has run out of pastrami")
missing_order = 'pastrami'
while missing_order in sandwich_orders:
	sandwich_orders.remove(missing_order)
print(sandwich_orders)
finished_sandwiches = []
for sandwich in sandwich_orders:
	finished_sandwiches.append(sandwich)
for sandwich_ready in finished_sandwiches:
	print(f"I made your {sandwich_ready}")

		
		
		


