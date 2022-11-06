# In the python shell, Create a variable called `my_age`, use python to know how old you will be in 123879 years

my_age = int(input("How old are you? "))
print(f"You would be {my_age + 123879} years old in 123879 years!")

# In the python shell, Create a variable called first_name and a variable called last_name, 
# and then print your full name using those two variables

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
print(f"Hello, {first_name} {last_name}!")

# Place a comment next to each variable. The comments will:


# Explain what each variable does
# Find out the type of each
# Format each variable into a print statement

cars = 100 #type INT
space_in_a_car = 4.0 #type FLOAT
drivers = 30 #type INT
passengers = 90 #type INT
cars_not_driven = cars - drivers #calculates how many cars are left by subtracting the drivers count
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car #calculates how many seats are available per car driven
average_passengers_per_car = passengers / cars_driven #calculates the average amount of passengers per car


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

#Analyze the code below and precit what the outcome will be. Check the results in your python shell.

age = input("How old are you? ")
print("You are {} years old".format(age)) #Will return a string with the user's age

# Ask the user for a number between 1 and 100
# If the number is a multiple of three, print "Fizz"
# If the number is a multiple of five, print "Buzz"
# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

i = int(input("Please choose a number between 1 and 100: "))
for i in range(1,101):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)
		
# OR

if i % 3 == 0:
	print("Fizz", end="") #By default Python after printing skips to the next line. With the end command, it won't
if i % 5 == 0:
	print("Buzz")
else:
	print(i)