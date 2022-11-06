'''Exercise 1: 

Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world
'''

print("Hello World\n"*4)

''' Exercise 2: 

Write code that calculates the result of: (99^3) * 8
'''

print(int((99^3)*8))

'''Exercise 3: Predict the output of the following code snippets:

5 < 3 #FALSE because 5 is bigger than 3
3 == 3 #TRUE because 3 is the same type and has the same value as 3
3 == "3" #FALSE because one is an integer and the other is a string, so two different types
"3" > 3 #ERROR because you can't compare two different types of values
"Hello" == "hello" #FALSE because the string is case sensitive
'''

#  Exercise 4: Create a variable called computer_brand which value is the brand name of your computer.
#  Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer"

computer_brand = input("What's your computer's brand? ")
print(f"You have a {computer_brand} computer.")

'''Exercise 5: 

Create a variable called name, and set it’s value to your name.
Create a variable called age, and set it’s value to your age.
Create a variable called shoe_size, and set it’s value to your shoe size.
Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
Have your code print the info message.
Run your code
'''

name = input("What's your name? ")
age = int(input("How old are you?"))
shoe_size = int(input("What's your shoe size?"))
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

'''Exercise 6:

Create two variables, a and b.
Each variables value should be a number.
If a is bigger then b, have your code print Hello World.
'''

a = int(input("Choose a number: "))
b = int(input(" Choose another number: "))
if a > b:
	print("Hello World")

'''Exercise 7: 

Write code that asks the user for a number and determines whether this number is odd or even.
'''

n = int(input("Choose a number: "))
if n % 2 == 0: #here can also be if n % 2 != 0: but then it would have to print Odd instead
	print("Even")
else:
	print("Odd")

'''Exercise 8:

Write code that asks the user for their name and determines whether or not you have the same name, 
print out a funny message based on the outcome.
'''

name = input("What's your name? ")
if name.lower() == 'ronny':
  print("Samesies! Mommy must be confused!")
else:
  print(f"Hello {name}!")

'''Exercise 9:

Write code that will ask the user for their height in inches.
If they are over 145cm print a message that states they are tall enough to ride.
If they are not tall enough print a message that says they need to grow some more to ride.
'''

print("Please input your height: ")
h_feet = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_feet*12
h_cm = round(h_inch *2.54, 1) # here the height is being converted to cm and the result is being rounded to the nearest whole number
print(f"Your height is : {h_cm} cm.")

if h_cm > 145:
  print("Enjoy the ride!")
else:
  print("Sorry, you're not tall enough to ride. Maybe next time!")