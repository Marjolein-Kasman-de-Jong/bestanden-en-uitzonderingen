# Opdracht 10-3 Gast

user_input = input('Hoe heet je? ')

filename = 'text_files/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(user_input)