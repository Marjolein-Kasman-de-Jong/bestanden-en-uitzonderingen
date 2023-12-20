# Opdracht 10-12 Favoriete getal onthouden

import json

filename = 'json_files/favorite_number.json'


def get_stored_favorite_number():
    """ Get stored favorite number if available """
    try:
        with open(filename, 'r') as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
            return None
    else:
        return "I know your favorite number! It's " + favorite_number + "."     


def get_new_favorite_number():
    """ Get favorite number from user """
    user_input = input('What is your favorite number? ')
    with open(filename, 'w') as file_object:
        json.dump(user_input, file_object)

def show_favorite_number():
    """ Show the user's favorite number """
    user_input = get_stored_favorite_number()
    if user_input:
        print(user_input)
    else:
        user_input = get_new_favorite_number()
        print("I will remember your favorite number!")

show_favorite_number()