'''Exercise:

Write a program to reverse the sentence wordwise.

Input:
You have entered a wrong domain
Output:
domain wrong a entered have You
'''

def reverse_input():
  user_input = input('Please write a sentence: ')
  words_list = user_input.split(' ')
  words_list.reverse()
  reverse_sentence = " ".join(words_list)
  return(reverse_sentence)
print(reverse_input())