import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("",key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add",size=10)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(),key="todos_list",
                      enable_events=True, size = [45,10])

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica",15))

while True:
    event, values = window.read(timeout=300)
    window["clock"].update(time.strftime("%b %d, %Y %H:%M:%S"))

    '''print(1, "event = ",event)
    print(2, "values of the event = ", values)
    print(3, "written value = ", values["todos_list"])'''

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"].capitalize() + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window["todos_list"].update(values=todos)

    elif event == "Edit":
        try:
            todos = functions.get_todos()
            new_todo = values["todo"].capitalize() + "\n"
            todo_to_edit = values["todos_list"][0]
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos_list"].update(values=todos)
        except IndexError:
            sg.popup("Please select todo.",font=("Helvetica",15))

    elif event == "Complete":
        try:
            todos = functions.get_todos()
            todo_to_complete = values["todos_list"][0]
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos_list"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("Please select todo.",font=("Helvetica",15))

    elif event == "todos_list":
        window["todo"].update(value=values["todos_list"][0])

    elif event == "Exit":
        break

    elif event == sg.WINDOW_CLOSED:
        break

window.close()

