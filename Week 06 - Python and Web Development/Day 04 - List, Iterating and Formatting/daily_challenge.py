from datetime import datetime, timedelta, date
bday = input('Please write your birthday using the DD/MM/YYYY format: ')
bdate = datetime.strptime(bday, "%d/%m/%Y")
cdate = datetime.now()
age = cdate.year - bdate.year
if cdate.month < bdate.month:
  age = age - 1
  print(f'You are {age} years old!')
else:
  print(f'You are {age} years old!')
str_age = str(age)
candle_count = int(str_age[-1])*'i'

if (bdate.year % 4 == 0 and bdate.year %  100 != 0) or (bdate.year % 400 == 0):
  print(f'       ___{candle_count}___\n      |:H:a:p:p:y:|\n    __|___________|__\n   |^^^^^^^^^^^^^^^^^|\n   |:B:i:r:t:h:d:a:y:|\n   |                 |\n   ~~~~~~~~~~~~~~~~~~~\n'*2)
else:
  print(f'       ___{candle_count}___\n      |:H:a:p:p:y:|\n    __|___________|__\n   |^^^^^^^^^^^^^^^^^|\n   |:B:i:r:t:h:d:a:y:|\n   |                 |\n   ~~~~~~~~~~~~~~~~~~~\n')