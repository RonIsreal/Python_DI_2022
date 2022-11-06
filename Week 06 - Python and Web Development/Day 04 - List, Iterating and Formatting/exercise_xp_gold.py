'''Exercise 1:

Write code that concatenates two lists together without using the + sign.
'''

list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list1.extend(list2)
print(list1)

'''Exercise 2:

Ask the user for 3 numbers and print the greatest number.
    Test Data
    Input the 1st number: 25
    Input the 2nd number: 78
    Input the 3rd number: 87

    The greatest number is: 87
'''

numbers_list = []
while len(numbers_list) != 3:
    chosen_number = float(input("Please choose a number: "))
    numbers_list.append(chosen_number)
sorted_list = sorted(numbers_list, reverse = True) #Here we sort the list in descending order (because of the parameter reverse = True)
print("The biggest number you chose is " + str(sorted_list[0]))

'''Exercise 3:

Create a string of all the letters in the alphabet
Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
'''

import string

my_list = list(string.ascii_lowercase) #Create a list with all letters using the module "string" that was imported
vowels = ('a', 'e', 'i', 'o', 'u')
while True:
    for letter in my_list:
        if letter in vowels:
            print(f"'{letter.upper()}' is a vowel.")
        else:
            print(f"'{letter.upper()}' is a consonant.")
    break

'''Exercise 4:

Using this variable

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
Example: if input is 'Cortana' we should be printing the index 1
'''

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
your_name = input("What's your name? ")
if your_name in names:
    print(names.index(your_name))
    
'''Exercise 5:

Ask a user for 7 words, store them in a list named words.
Ask the user for a single character, store it in a variable called letter.
Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
'''

words = []
letter = input("Please choose a letter: ")
while len(words) != 7:
    words.append(input("Please write a word: "))
for word in words:
    if letter in word:
        print(word.index(letter))
    else:
        print(f"Nice! Your word {word} doesn't have the letter {letter}.")

'''Exercise 6:

Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million.
Use the sum() function to see how quickly Python can add a million numbers
'''

mynumbers = list(range(1,1000001))
for number in numbers:
    print(number)
print(min(mynumbers))
print(max(mynumbers))
print(sum(mynumbers))

'''Exercise 7:

Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
Suppose the following input is supplied to the program: 34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

mylist = list(input(" Please write a sequence of any numbers separated by comma: ").split(','))
print(mylist)
print(tuple(mylist))

'''Exercise 8:

Ask the user to input a number from 1 to 9 (including).
Get a random number between 1 and 9. Hint: random module.
If the user guesses the correct number print a message that says Winner.
If the user guesses the wrong number print a message that says better luck next time.
Bonus: use a loop that allows the user to keep guessing until they want to quit.
Bonus 2: on exiting the loop tally up and display total games won and lost.
'''

import random

def playgame():
  
  games_played = 1
  random.seed()
  target_number = random.randint(1,9)
  
  tip = input("Do you want a hint? (Yes/No): ")
  if tip.lower() != 'yes':
    print("Ok. Good luck!")
  else:
    if target_number in range(1,5):
      print("The right number is between 1 and 5...")
    else:
      print("The right number is between 6 and 9...")
  
  guess_number = int(input("Which number is the right one? "))
  
  if guess_number < target_number:
    print("Too low! Better luck next time!")
    another_one = input("Would you like to play again? (Yes/No): ")
    if another_one.lower() == 'yes':
      games_played += 1
      print(f"You have played {games_played} times.")
      playgame()
    else:
      print(f"You have played {games_played} times.")
      print("Game Over!")
      
  elif guess_number > target_number:
    print("Too high! Better luck next time!")
    another_one = input("Would you like to play again? (Yes/No): ")
    if another_one.lower() == 'yes':
      games_played += 1
      print(f"You have played {games_played} times.")
      playgame()
    else:
      games_played += 1
      print(f"You have played {games_played} times.")
      print("Game Over!")
    
  else:
    print("Congratulations! You guessed it!")
    another_one = input("Would you like to play again? (Yes/No): ")
    if another_one.lower() == 'yes':
      games_played += 1
      print(f"You have played {games_played} times.")
      playgame()
    else:
      games_played += 1
      print("Winner!")
      print(f"You have played {games_played} times.")

playgame()
