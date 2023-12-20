# Opdracht 10-11A Favoriete getal

import json

user_input = input('Wat is je favoriete getal? ')

filename = 'json_files/favorite_number.json'

with open(filename, 'w') as file_object:
    json.dump(user_input, file_object)
