# Opdracht 10-6 Optellen
# Opdracht 10-7 Optelcalculator

while True:
    user_input_1 = input('Voer getal 1 in: ')
    if user_input_1.lower() == 'q':
        break
    user_input_2 = input('Voer getal 2 in: ')
    if user_input_2.lower() == 'q':
        break
    try:
        result = int(user_input_1) + int(user_input_2)        
    except ValueError:
            print('Voer een GETAL in!')
    else:
       print(user_input_1 + " + " + user_input_2 + " = " + str(result))