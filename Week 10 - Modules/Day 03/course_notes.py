'''Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps

Read the file line by line
Read only the 5th line of the file
Read only the 5th first characters of the file
Read all the file and return it as a list of strings. Then split each word
Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
Append your first name at the end of the file
Append "SkyWalker" next to each first name "Luke"'''

f = open('nameslist.txt', 'r+')
lines = f.readlines()
print(lines)
print(lines[4])
print(lines[0][4])

for line in lines:
    if len(line) >= 5:
        print(line[4])
    else:
        if line[-1] != "":
            print(line[-1])

darth_count = 0
luke_count = 0
lea_count = 0

for line in lines:
    if line == 'Luke\n':
        line.join(" Skywalker")
        luke_count += 1
    elif line == 'Lea\n':
        lea_count += 1
    else:
        darth_count += 1

print(luke_count, lea_count, darth_count)
f.write("Ronny")
