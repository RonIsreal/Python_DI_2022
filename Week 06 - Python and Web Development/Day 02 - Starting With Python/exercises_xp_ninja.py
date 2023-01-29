'''Exercises 1, 2 and 3 were done at the console'''

'''Exercise 4:

Use python to find out how many characters are in the following text, 
use a single line of code (beyond the establishment of your my_text variable).
'''
my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.'''

print(len(my_text))

'''Exercise 5:

Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
'''

def no_a():

	my_input = input("Please write the longest sentence or word you can without using the letter 'A': ")
	input_length = len(my_input)
	last_length = 0
	repeat = True
	for letter in my_input.lower():
		if letter == 'a':
			repeat == False
			print('Busted!')
			break
		else:
			if input_length > last_length:
				print("Nice!")
				last_length = len(my_input)
				if repeat == True:
					no_a()
				else:
					pass
	print(input_length)





no_a()
