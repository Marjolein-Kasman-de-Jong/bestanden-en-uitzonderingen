# Opdracht 10-8 Cats and Dogs
# Opdracht 10-9 Cats and Dogs (in stilte)

filenames = ['text_files/cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
