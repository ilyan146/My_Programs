FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the text file and make the file content it into  a list!"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines() # Creates a list called todos in read mode which will add the present data in text file so its not lost
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to-dos that have been amended in the program into the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


freezing_point = 0
boiling_point = 100


def water(temp):
    if temp <= freezing_point:
        return "Solid"
    elif temp >= boiling_point:
        return "Gas"
    else:
        return "Liquid"


if __name__ == "__main__":
    print("Hello functions file is now active!!")
    print(get_todos())