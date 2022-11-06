'''Exercise 1:

Continuation of the Exercise 2 XP NINJA - from Week4Day2

Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
Will the code work when the number of random numbers is not equal to 10?

'''
import random
random.seed()

mynumbers = []
while len(mynumbers) != random.randint(10,30):
    mynumbers.append(random.randint(-100,100))
print(mynumbers)

print(f"My numbers list: {mynumbers}")

print(f"My numbers sorted: {sorted(mynumbers, reverse = True)}")

print(f"My list summed: {sum(mynumbers)}")

print(f"First and last numbers in my list: {[mynumbers[0], mynumbers[-1]]}")

toplist = []
lowerlist = []
for number in mynumbers:
  if number > 50:
    toplist.append(number)
  else:
    lowerlist.append(number)
print(f"Numbers lower than 50 in my list: {lowerlist}")
print(f"Numbers higher than 50 in my list: {toplist}")

squaredlist = []
for number in mynumbers:
  squaredlist.append(number**2)
print(f"Numbers in my list squared: {squaredlist}")

list_set = set(mynumbers)
print(f"My list without any duplicates: {list_set}")

print(f"My list was {len(mynumbers)} numbers long. Without any duplicates the list is now {len(list_set)} numbers long.")

list_average = sum(mynumbers) / len(mynumbers)
print(f"The average value of my list is {list_average}")

print(f"The smallest number in the list is {sorted(mynumbers)[0]} and the biggest is {sorted(mynumbers)[-1]}.")

'''Exercises 2 and 3:

Create a dictionary that contains users: each key will represent a username, and each value will represent that user’s password. Initialize this dictionary with 3 users & passwords.
Create a loop that does the following:
If the user inputs “exit”, break out of the loop.
If the user inputs “login”, ask them for their username and password.
If the user’s details exist print “you are now logged in”.
If the user is successfully logged in, store the username in a variable called logged_in so we can track it later.
If the user does not exist ask if they would like to sign up:
Ask the user for a username and make sure it doesn’t exist as a key in our dictionary, if the username is not valid continue asking the user to input a username.
Ask the user for a password. The password is the value.
'''

user_list = {
    
    'Ronny': 'xecucleiclei',
    'lenA': 'alfred',
    'MaX': 'munchie'
}

logged_in = []

def user_in():
    
  user_input = input("Please choose if you would like to 'login' or 'exit': ").lower()
  if user_input == 'login':
    print("Connecting...")
    connect()
  elif user_input == 'exit':
    print("Closing the application...")
  else:
    print("Invalid input. Please specify if you would like to 'login' or 'exit': ")
    user_in()
    
def connect():
  
  username = input("Please input your username (case sensitive): ")
  if username in user_list:
    print("Username found.")
    get_pass(username)
  else:
    print("Username not found.")
    reg_input = input("Would you like to register? (Yes/No)").lower()
    if reg_input == 'no':
      connect()
    elif reg_input == 'yes':
      make_new_user()
    else:
      print("Invalid input.")
      connect()
      
    
def get_pass(username):
  
  userpass = input("Please input your password: ")
  if user_list[username] == userpass:
     print("Connected!")
     logged_in.append(username)
  else:
     print("Wrong password.")
     get_pass(username)

def make_new_user():
  while True: 
    username = input("Please write your username: ")
    if username in user_list:
      print("This username is already taken.")
    else:
      print("Username available.")
      break 
  password = input("Please type your password: ")
  user_list[username] = password
  connect() 

user_in()

print(logged_in)
print(user_list)
    
