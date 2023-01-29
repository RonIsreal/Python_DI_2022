'''Exercise 1 : Built-In Functions
Instructions
Python has many built-in functions.
If you feel that you don’t know how to properly implement them take a look at the python documentation online.

Write a program which prints the results of the following python built-in functions: abs(), int(), input().
Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.'''

class Object:

    '''abs() function will return the absolute value of the input
int() function will return the integer value of the input
input() function will prompt the user to input a numeric value'''

    def __init__(self,number):
        self.number = int(input("Please choose a number: "))

    def __abs__(self):
        return f"'{self.number}'"

    def __int__(self):
        return self.number



test_object = Object(-10)
print(abs(test_object))
print(int(test_object))
print(test_object.__doc__)

'''🌟 Exercise 2: Currencies
Instructions'''

class CurrencyExmple:
    def __init__(self, currencyx, amountx):
        self.currencyx = currencyx
        self.amountx = amountx

    #Your code starts HERE


'''Using the code above, implement the relevant methods and dunder methods which will output the results below.
Hint : When adding 2 currencies which don’t share the same label you should raise an error.
>>> c1 = Currency('dollar', 5)
>>> c2 = Currency('dollar', 10)
>>> c3 = Currency('shekel', 1)
>>> c4 = Currency('shekel', 10)

>>> str(c1)
'5 dollars'

>>> int(c1)
5

>>> repr(c1)
'5 dollars'

>>> c1 + 5
10

>>> c1 + c2
15

>>> c1 
5 dollars

>>> c1 += 5
>>> c1
10 dollars

>>> c1 += c2
>>> c1
20 dollars

>>> c1 + c3
TypeError: Cannot add between Currency type <dollar> and <shekel>'''

class Currency:

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.currency} {self.amount}"

    def __add__(cls, other):
        if isinstance(other, int):
            return cls.amount + other
        elif isinstance(other, Currency):
            return cls.amount + other.amount


c1 = Currency('dollars', 5)
c2 = Currency('dollars', 10)
c3 = Currency('shekels', 1)
c4 = Currency('shekels', 10)
print(c1 + 5)
print(c1 + c2)
print(str(c1))