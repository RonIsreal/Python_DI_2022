'''Notice : solve this exercise using a lambda function.

Ask a user for the following inputs 5 times:
Name (string)
Age (int)
Score (int)
Build a list of tuples using these inputs, each tuple should contain a name, age and score.
Sort the list by the following priority Name > Age > Score.
If the following tuples are given as input to the script:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
Note : The lambda function will not print but sort'''

def choosenames():
    count = 0
    while count < 5:
        addname = input("Please choose a name: ")
        names.append(addname)
        count += 1

def chooseages():
    a_count = 0
    while a_count < 5:
        addage = input("Please choose an age: ")
        ages.append(addage)
        a_count += 1

def choosescores():
    s_count = 0
    while s_count < 5:
        addscore = input("Please choose a score: ")
        scores.append(addscore)
        s_count += 1

def doall():

    choosenames()
    chooseages()
    choosescores()


names = []
ages = []
scores = []
doall()
full_users = list(zip(names, ages, scores))
full_users.sort(key= lambda x: x[0])
print(full_users)