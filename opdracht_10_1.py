# Opdracht 10-1 Python leren

filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

learning_python_string = ''

for line in lines:
    learning_python_string += line

print(learning_python_string)