'''Challenge 1
Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
Examples

number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]'''

user_number = int(input("Please choose a number : "))
user_length = int(input("Please choose a length: "))

table_list = [user_number * i for i in range(1,user_length+1)]
print(table_list)

'''Challenge 2
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
Examples

user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"'''

user_word = input("Please enter a word: ")
new_word = ""

for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i-1]:
        new_word += user_word[i]

print(new_word)