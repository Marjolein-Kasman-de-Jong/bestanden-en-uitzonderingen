# Opdracht 10-5 Enquête over programmeren

running = True

while running:
    user_input = input('Waarom hou je van programmeren (voer Q in om af te sluiten)? ')
    if user_input.lower() == 'q':
        running = False
    else:
        with open('text_files/reasons_to_like_coding.txt', 'a') as file_object:
            file_object.write(user_input + "\n")