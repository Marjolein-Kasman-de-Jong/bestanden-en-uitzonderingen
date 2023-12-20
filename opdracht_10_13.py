# Opdracht 10-13 Gebruiker verifiëren

import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'json_files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def check_username(username):
    """ Check if username is correct"""
    check = input("Are you " + username + "? Y/N ")
    correct_username = ''
    if check.lower() == 'n':
        correct_username = get_new_username()
    else:
        correct_username = username
    return correct_username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'json_files/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    message = ''
    if username:
        correct_username = check_username(username)
        if username == correct_username:
            message = "Welcome back, " + correct_username + "!"
        else:
            message = "We'll remember you when you come back, " + correct_username + "!"
    else:
        correct_username = get_new_username()
        message = "We'll remember you when you come back, " + correct_username + "!"
    print(message)


greet_user()
