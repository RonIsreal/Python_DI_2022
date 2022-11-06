'''

Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.

Then, print the first and last characters of the given text.

Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "Hello World"
Then, you have to construct the string character by character
H
He
Hel
... etc
Hello World


4. Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

Hlrolelwod
'''
import random

strg = input("Please write something in 10 characters (spaces count too)")
i = 0
if len(strg) < 10:
  print("Your text is too short")
elif len(strg) > 10:
  print("Your text is too long")
else:
  print(f"First letter: {strg[0]}")
while i < len(strg):
	print(strg[i] + strg[i + 1])
	i += 1
strg_list = list(strg)
random.shuffle(strg_list)
mix_strg = "".join(strg_list)
print(mix_strg)

#PENDING CORRECTION THIRD PART ONLY