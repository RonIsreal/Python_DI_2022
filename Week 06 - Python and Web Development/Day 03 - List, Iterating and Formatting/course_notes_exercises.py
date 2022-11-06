'''Exercise 1:

Given this list: list1 = [5, 10, 15, 20, 25, 50, 20],
find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
'''

list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3] = 200
print(list1)

'''Exercise 2:

Unpack the following tuple into 4 variables


a_tuple = (10, 20, 30, 40)
'''

a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple
print(a)
print(b)
print(c)
print(d)

'''Exercise 3:

Accept a number from the user and print its multiplication table
'''

num = int(input("Please choose a number"))
for i in range(1,11):
  print(num*i)

'''Exercise 4:

Print the numbers from 1 to 10 using while loop
'''

for i in range (1,11):
  print(i)