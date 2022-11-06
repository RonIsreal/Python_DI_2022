'''Exercise 1:

Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world
I love python
I love python
I love python
I love python
'''

print("Hello World\n"*4+"I love Python\n"*4)

'''Exercise 2:

Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)
'''

month = int(input("Please choose a month from 1 until 12: "))
if month in range(1,13):
  if month in range(3, 6):
    print("Spring")
  elif month in range(6, 9):
    print("Summer")
  elif month in range(9, 12):
    print("Autumn")
  else:
    print("Winter")
else:
  print("Not a valid month.")

# my first resolution was using a more Javascript line of thought by creating ifs with two conditionals,
# for example, if month <= 5 and month >= 3: print("Spring") and if the month value would be equal or bigger than 13,
# it would return the 'Not valid month' error