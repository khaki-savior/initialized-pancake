initial_menu = 'Hello, user_name\nCommands: \nadd, \ndelete, \nupdate, \nlist, \nmark-in-progress, \nmark-done'

while True:
    print(initial_menu)
    user_input = input()
    if user_input == 'home': print(initial_menu)
    if user_input == 'add': input('add task with ID:')
    if user_input == 'delete': input('delete task with ID:')
    if user_input == 'update': input('update task with ID')
    if user_input == 'list': 
        if user_input == 'todo': pass
        if user_input == 'in-progress': pass
        if user_input == 'done': pass
    if user_input == 'mark-in-progress': input('mark task with ID:')
    if user_input == 'mark-done': input('mark task with ID:')
    if user_input == 'q': break