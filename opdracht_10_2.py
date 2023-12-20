# Opdracht 10-2 C leren

filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

learning_python_string = ''
for line in lines:
    line = line.replace('Python', 'C')
    learning_python_string += line

print(learning_python_string)