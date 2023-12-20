# Opdracht 10-11B Favoriete getal

import json

filename = 'json_files/favorite_number.json'

with open(filename, 'r') as file_object:
    favorite_number = json.load(file_object)
    message = "I know your favorite number! It's " + favorite_number + "!"
    print(message)