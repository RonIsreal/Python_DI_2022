'''Exercise 1:

Instructions

A - Draw the following pattern using for loops:
  *
 ***
*****


B - Draw the following pattern using for loops:
    *
   **
  ***
 ****
*****


C - Draw the following pattern using for loops:
*
**
***
****
*****
*****
 ****
  ***
   **
    *
'''
# A

size = 4
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = "*"
        print(character, end=' ')
    print(" ")

# B
rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print("*", end=' ')
            num += 1
    print("")

# C

# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")
rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1

'''Exercise 2: 

Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
'''

my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1): #Find the Range to count the indexes
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]): #Compare each number inside the list
            minimum = j #Assign a new value to variable minimum if the value is lower than the previous one
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] #Sort all items inside the list from lower to highest
print(my_list)

