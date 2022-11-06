''' Exercise 1:

Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
******************
* Hello          *
* World          *
* in             *
* reallylongword *
* a              *
* frame          *
******************'''


text = input("Please write your sentence: ")
def box_printer(words):
    box_size = len(max(words, key=len))
    print('*' * (box_size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=box_size))
    print('*' * (box_size + 4))

box_printer(text.split(' '))

'''Exercise 2:

Analyse this code before executing it. What is the purpose of this code?

def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)


'''
# The purpose of this code is to sort the values inside the list by ascending order.