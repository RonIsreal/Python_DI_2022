'''Exercise:

A perfect number is a positive integer that is equal to the sum of its divisors.
However, the number itself is not included in the sum.

Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
Hint: Google perfect numbers
Example

Input -- Enter the number:6
Output -- True

Input -- Enter the number:10
Output --  False
'''

def perfect_number():
    n = int(input("Please write a number: "))
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number())