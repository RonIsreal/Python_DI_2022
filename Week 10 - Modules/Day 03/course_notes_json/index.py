import json

json_file = 'file.json'
with open(json_file, 'r+') as file_obj:
    family = json.load(file_obj)

print(f"{family['firstName']} is {family['age']}. She has two adorable kids named {family['children'][0]['firstName']} and {family['children'][1]['firstName']}.")

upd_dict = {'favourite_color': 'red'}
children = family['children']
children.append(upd_dict)
print(children)

