# Opdracht 10-10 Bekende woorden

books = ['text_files/a_christmas_carol.txt', 
         'text_files/pride_and_prejudice.txt', 
         'text_files/dracula.txt']

for book in books:
    try:
        with open(book, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        number_of_the = contents.lower().count('the')
        print(number_of_the)