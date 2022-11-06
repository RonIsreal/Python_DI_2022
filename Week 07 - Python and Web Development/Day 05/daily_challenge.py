'''Exercise 1: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension
Example:

Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world'''

my_list = list(input("Please choose some words and separate them with a comma: ").split(","))
sorted_list = sorted([x for x in my_list])
print(sorted_list)