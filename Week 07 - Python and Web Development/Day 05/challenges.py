import math

'''Exercise 1: Write a script that inserts an item at a defined index in a list.'''

my_list = ['a', 'e', 'o', 'u']

def insert_in_list():
    where_in_list = int(input("Please choose a position using numeric values only: "))
    item = input("Please write what you would like to add to the current list: ")
    my_list.insert(where_in_list, item)
    return my_list

insert_in_list()
print(my_list)

'''Exercise 2: Write a script that counts the number of spaces in a string.'''

my_string = input("Please write whatever comes to mind: ")

def count_spaces():
    space_count = my_string.count(" ")
    return space_count

print(count_spaces())

'''Exercise 3: Write a script that calculates the number of upper case letters and lower case letters in a string.'''

the_string = input("Please write something using upper and lower case letters: ")

def count_cases():
    lower_cases = sum(map(str.islower, the_string))
    upper_cases = sum(map(str.isupper, the_string))
    return print(f"Lower cases: {lower_cases}, Upper cases: {upper_cases}")

count_cases()

'''Exercise 4: Write a function to find the sum of an array without using the built in function:'''

my_sum = [1, 5, 4, 2]

def sum_list():
    sum = 0
    for items in my_sum:
        sum += items
    print(sum)

sum_list()

'''Exercise 5: Write a function to find the max number in a list'''

find_max = [0, 1, 3, 50]

def find_highest():
    highest_num = max(find_max)
    return highest_num

print(find_highest())


'''Exercise 6: Write a function that returns factorial of a number'''

def calculate_factorial():
    number = math.factorial(int(input("Please choose a number: ")))
    return number

print(calculate_factorial())

'''Exercise 7: Write a function that counts an element in a list (without using the count method):'''

list_count = [('a', 'b', 'c'), 'd']

def count_list():
    list_sum = 0
    for items in list_count:
        list_sum += 1
    return list_sum

print(count_list())

'''Exercise 8: Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:'''

norm = [1, 2, 2]

def calc_l2():
    sum = 0
    for items in norm:
        sum += items**2
    sqrt_result = math.sqrt(sum)
    return sqrt_result


print(calc_l2())

'''Exercise 9: Write a function to find if an array is monotonic (sorted either ascending of descending)

>>>is_mono([7,6,5,5,2,0])
    >>>True

    >>>is_mono([2,3,3,3])
    >>>True

    >>>is_mono([1,2,0,4])
    >>>False'''

is_mono_one = [7,6,5,5,2,0]
is_mono_two = [2,3,3,3]
is_mono_three = [1,2,0,4]

def is_monotonic(your_list):

    for items in your_list:
        if your_list == sorted(your_list):
            return True
        elif your_list == sorted(your_list, reverse = True):
            return True
        else:
            return False

print(is_monotonic(is_mono_one))
print(is_monotonic(is_mono_two))
print(is_monotonic(is_mono_three))

'''Exercise 10: Write a function that prints the longest word in a list.'''

def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word

'''Exercise 11: Given a list of integers and strings, put all the integers in one list, and all the strings in another one.'''

def sort_types(mixed_list):
    sorted_ints = []
    sorted_strs = []
    for items in mixed_list:
        if isinstance(items, str):
            sorted_strs.append(items)
        elif isinstance(items, int):
            sorted_ints.append(items)
        else:
            pass
    return sorted_strs, sorted_ints

print(sort_types(['a', '1', 1, 2, 'three', 4]))

'''Exercise 12: Write a function to check if a string is a palindrome:'''

def is_palindrome(word):
    if word == word[::-1]:
        return print("True")
    else:
        return print("False")

is_palindrome('natan')
is_palindrome('amor')

'''Exercise 13: Write a function that returns the amount of words in a sentence with length > k:

    >>>sentence = 'Do or do not there is no try'
    >>>k=2
    >>>sum_over_k(sentence,k)
    >>>3'''


def find_words(sentence, k):
    count = 0
    words = list(sentence.split(" "))
    for word in words:
        if len(word) > k:
            count += 1
    return count


print(find_words("Do or do not there is no try", 2))

'''Exercise 14: Write a function that returns the average value in a dictionary (assume the values are numeric)'''

dict_avg = {'a': 1, 'b': 2, 'c': 8, 'd': 1}

def find_avg(your_dict):
    total_sum = 0
    total_avg = 0
    for v in your_dict.values():
        total_sum += v
    total_avg = total_sum / len(your_dict)
    return total_avg

print(find_avg(dict_avg))

'''Exercise 15: Write a function that returns common divisors of 2 numbers:

    >>>common_div(10,20)
    >>>[2,5,10]'''

def common_div(num1, num2):
    numrange = 0
    common_divs = []
    if num1 > num2:
        numrange = range(2, num1+1)
    else:
        numrange = range(2, num2+1)
    for n in numrange:
        if num1 % n == 0 and num2 % n == 0:
            common_divs.append(n)
    return common_divs

print(common_div(10,20))

'''Exercise 16: Write a function that test if a number is prime:

    >>>is_prime(11)
    >>>True'''

def is_prime(numb):
    if numb > 1:
        for n in range (2, numb):
            if (numb % n) == 0:
                return False
                break
            else:
                return True
    else:
        return False
print(is_prime(7))

'''Exercise 17: Write a function that prints elements of a list if the index and the value are even:

    >>>weird_print([1,2,2,3,4,5])
    >>>[2,4]'''

def find_evens(your_list):
    all_evens = []
    for index, item in enumerate(your_list):
        if index % 2 == 0 and item % 2 == 0:
            all_evens.append(item)
    return all_evens

print(find_evens([1,2,2,3,4,5]))

'''Exercise 18: Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

    >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
    >>>int: 1, str:1 , float:1, bool:2'''


def type_count(list):
    int_count = 0
    str_count = 0
    float_count = 0
    bool_count = 0
    for item in list:
        if isinstance(item, bool):
            bool_count += 1
        elif isinstance(item, int):
            int_count += 1
        elif isinstance(item, str):
            str_count += 1
        elif isinstance(item, float):
            float_count += 1
        else:
            pass
    print(f"int: {int_count}, str: {str_count}, float: {float_count}, bool: {bool_count}")


type_count([1, 'string', 1.0, True, False])

# OR

from collections import Counter

print(Counter(type(x).__name__ for x in [1,'string',1.0,True,False]))

'''Exercise 19: Write a function that mimics the builtin .split() method for strings.
By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.'''


def split(string, delimiters=' '):
    result = []
    words = ''
    for char in string:
        if char not in delimiters:
            words += char
        elif words:
            result.append(words)
            words = ''

    if words:
        result.append(words)

    return result


print(split('The wine is expensive'))
print(split('The wine is expensive','e'))

'''Exercise 20: Convert a string into password format.
Example:
input : "mypassword"
output: "***********"'''

def passwordify(string):
    return "*" * len(string)

print(passwordify("password"))





