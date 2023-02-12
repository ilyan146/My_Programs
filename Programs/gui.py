import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(),key="todos_list",
                      enable_events=True, size = [45,10])

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=("Helvetica",20))

while True:
    event, values  = window.read()
    print(1, "event = ",event)
    print(2, "values of the event = ", values)
    print(3, "written value = ", values["todos_list"])

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window["todos_list"].update(values=todos)

    elif event == "Edit":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todo_to_edit = values["todos_list"][0]
        index = todos.index(todo_to_edit)

        todos[index] = new_todo
        functions.write_todos(todos)
        window["todos_list"].update(values=todos)

    elif event == "todos_list":
        window["todo"].update(value=values["todos_list"][0])


    elif event == sg.WINDOW_CLOSED:
        break


window.close()

