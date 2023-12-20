# Opdracht 10-4 Gastenboek

running = True

while running:
    user_input = input('Hoe heet je (voer Q in om af te sluiten)? ')
    if user_input.lower() == 'q':
        running = False
    else:
        print('Hallo, ' + user_input + '!')
        with open('text_files/guest_book.txt', 'a') as file_object:
            file_object.write(user_input + "\n")