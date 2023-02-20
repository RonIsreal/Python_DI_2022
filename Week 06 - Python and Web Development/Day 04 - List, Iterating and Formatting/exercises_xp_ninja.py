'''Exercise 1:

Write a program that calculates and prints a value according to this given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
For example, if the user inputs: 100,150,180
The output should be:

18,22,24
'''

from math import sqrt

c = 50
h = 30
results = []
numbers = input("Please choose any numbers separated by comma.").split(',')
for number in numbers:
    results.append(round(sqrt((2*c*int(number))/h)))
print(results)

'''Exercise 2:

Given a list of 10 integers to analyze. For example:

    [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
    [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
    [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
    [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
    
Store the list of numbers in a variable.
Print the following information:
a. The list of numbers – printed in a single line
b. The list of numbers – sorted in descending order (largest to smallest)
c. The sum of all the numbers
A list containing the first and the last numbers.
A list of all the numbers greater than 50.
A list of all the numbers smaller than 10.
A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
The numbers without any duplicates – also print how many numbers are in the new list.
The average of all the numbers.
The largest number.
The smallest number.
Bonus: Find the sum, average, largest and smallest number without using built in functions.
Extra bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100.
Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
'''

mynumbers = []
while len(mynumbers) != 10:
    mynumbers.append(int(input("Please choose a number between -100 and 100: ")))
print(mynumbers)

print(f"My numbers list: {mynumbers}")

print(f"My numbers sorted: {sorted(mynumbers, reverse = True)}")

print(f"My list summed: {sum(mynumbers)}")

print(f"First and last numbers in my list: {[mynumbers[0], mynumbers[-1]]}")

toplist = [i for i in mynumbers if i > 50]
lowerlist = [i for i in mynumbers if i <= 50]
print(f"Numbers lower than 50 in my list: {lowerlist}")
print(f"Numbers higher than 50 in my list: {toplist}")

squaredlist = [i**2 for i in mynumbers]
print(f"Numbers in my list squared: {squaredlist}")

list_set = set(mynumbers)
print(f"My list without any duplicates: {list_set}")

print(f"My list was {len(mynumbers)} numbers long. Without any duplicates the list is now {len(list_set)} numbers long.")

list_average = sum(mynumbers) / len(mynumbers)
print(f"The average value of my list is {list_average}")

print(f"The smallest number in the list is {sorted(mynumbers)[0]} and the biggest is {sorted(mynumbers)[-1]}.")

'''Exercise 3:

Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
Paste it to your code, and store it in a variable.
Let’s analyze the paragraph. Print out a nicely formatted message saying:
How many characters it contains (this one is easy…).
How many sentences it contains.
How many words it contains.
How many unique words it contains.
Bonus: How many non-whitespace characters it contains.
Bonus: The average amount of words per sentence in the paragraph.
Bonus: the amount of non-unique words in the paragraph.
'''

paragraph = '''

but i stood paralized,
on the supposed golden path,
and i was confronted,
by powerful demon force,
and there was the devil,
and we spoke his words,
flowed like glowing lava from the mouth of a volcano
'''

print(f"There are {len(paragraph)} characters in this paragraph.")

for sentences in paragraph:
  sentences = len(paragraph.split(","))
print(f"There are {sentences} sentences in this paragraph.")

for words in paragraph:
  words = len(paragraph.split(" "))
print(f"There are {words} words in this paragraph.")

unique_words = set(paragraph)
print(f"There are {len(unique_words)} unique words in this paragraph.")

paragraph_nospaces = [letter for letter in paragraph if letter != " "]
print(f"There are {len(paragraph_nospaces)} characters (not counting white space) in this paragraph.")

words_list = list(paragraph.split(" "))
paragraphs_paragraph = list(paragraph.split(","))
avg_wps = len(words_list) / len(paragraphs_paragraph)
print(f"The average amount of words per sentence in this paragraph is approximately {round(avg_wps)} words.")

print(f"The amount of non unique words in this paragraph is {len(paragraph.split(' ')) - len(unique_words)} words.")

'''Exercise 4:

Write a program that prints the frequency of the words from the input.

Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1
'''

user_input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words = user_input.split(" ")
words_frequency = []
for word in words:
    words_frequency.append(words.count(word))
results = dict(zip(words, words_frequency))
for k, v in results.items():
    print(f"{k} : {v}\n")


