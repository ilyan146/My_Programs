#from FUNCTIONS import get_todos,write_todos()
#This method is great when you only few functions!
import functions
"""
This method is preffered becasue it is kind of documentation
that lets the reader know the methods used such as get_todos()
is from that module and if there is a lot of functions in the file,
you dont have to import them all by mentioning separately using the method 1 above.
"""

import time
time_now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is now {time_now}")


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        #file = open('todos.txt','r')
        #todos = file.readilnes()
        #file.close()

        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        #new_todos = [i.strip("\n") for i in todos]

        for index,i in enumerate(todos):
            i = i.title()
            i = i.strip("\n")
            row = f"{index+1}-{i}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            index= number - 1
            new_todo = input("Enter new to do: ")
            todos = functions.get_todos()
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Command is not valid, please enter number of todo item.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            functions.write_todos(todos)
            print(f"The todo that is completed is {todo_to_remove.capitalize()}")
        except ValueError or IndexError:
            print("Command is invalid, please enter number of todo to be completed!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!!, please enter the requested option")

print("BYE!")

