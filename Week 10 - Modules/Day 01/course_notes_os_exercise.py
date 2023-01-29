'''Try to make a program that creates 5 directories, called `week1`, `week2`, ... , `week5`,
 in everyone of those directories, create 5 directories called `day1`, ...,
 `day5`, and in every day directory create two directories `lesson` and `homework`.'''

import os

print(os.getcwd())
# print(os.mkdir(r'C:\Users\Ronny\Desktop\Python Classes (2022)\Week 10 - Modules\Day 01\week1'))

def makedir():

    dir_count = 2
    while dir_count < 5:
        os.mkdir(r'C:\Users\Ronny\Desktop\Python Classes (2022)\Week 10 - Modules\Day 01\week'+str(dir_count))
        dir_count += 1

def makesubdir():
    f
