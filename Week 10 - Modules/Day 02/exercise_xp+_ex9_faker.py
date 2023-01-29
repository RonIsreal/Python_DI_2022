from faker import Faker

fk = Faker() #creates an instance of the faker module

users = []

def addUser(user_quant):
    while len(users) < user_quant:

        user_dict = dict({'name': fk.name(), 'address': fk.address(), 'language_code': fk.locale()})
        users.append(user_dict)
    return

addUser(2)
print(users)


