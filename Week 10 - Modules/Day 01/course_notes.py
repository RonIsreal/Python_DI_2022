'''Create a file called operators.py

Create 2 functions : addOperator(x,y) that returns the addition of 2 numbers, and divideOperator(x,y) that returns the division of 2 numbers

Create another file called calculator.py, and import the operators module. Call the 2 functions and display the results

Do this process 3 times :

once by importing the whole module
the second time by importing specific functions
the third time by using alias'''

import datetime
import operators
from operators import addOperator
from operators import divideOperator as do

print(operators.addOperator(4,2))
print(operators.divideOperator(4,2))
print(addOperator(6,3))
print(do(6,2))

'''Try to create a countdown to your birthday !

For example : "My birthday is in 45 days, and 10:29:46"'''

today_date = datetime.date.today()
my_bday = datetime.date(2023, 7, 20)
countdown = my_bday - today_date
print(countdown)
