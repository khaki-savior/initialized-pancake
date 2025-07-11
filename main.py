import os.path
import json
import time

user_input = input('action task_id "task_description":')

statuses = ['todo', 'in-progress', 'done']

def read_input():
    if user_input == 'help':
        pass

    if user_input == 'list':
        if status == 'done':
            pass
        elif status == 'todo':
            pass
        elif status == 'in-progress':
            pass
        else:
            pass

    if user_input == 'add':
        add_task()

    if user_input == 'update':
        pass

    if user_input == 'mark complete':
        pass

    if user_input == 'mark-in-progress':
        pass

    if user_input == 'complete':
        pass

    if user_input == 'delete':
        pass
#------------------------------------------------------------------------------------------------
def check_tasks_file_absent():
    file_path = os.path.join('data', 'tasks.json')
    if not os.path.exists(file_path):
        print("Файл tasks.json отсутствует в папке data")
        return True
    else:
        print("Файл tasks.json существует в папке data")
        return False
#------------------------------------------------------------------------------------------------
def add_task():
    pass
#------------------------------------------------------------------------------------------------
def get_next_task_id():
    pass
#------------------------------------------------------------------------------------------------
def save_new_task(task):

# Пример данных для записи
    initial_data = {
        "id": get_next_task_id(),
        "description": "A short description of the task",
        "status": statuses[0],
        "createdAt": time.strftime("%Y-%m-%d %H:%M"),
        "updatedAt": time.strftime("%Y-%m-%d %H:%M")
    }


def
# Пример данных для записи
    initial_data = {
        "id": 0,
        "description": "A short description of the task",
        "status": statuses[0],
        "createdAt": time.strftime("%Y-%m-%d %H:%M"),
        "updatedAt": time.strftime("%Y-%m-%d %H:%M")
    }
# Создаем JSON файл с данными
with open(os.path.join('data', 'tasks.json'), 'w', encoding='utf-8') as file:
    json.dump(initial_data, file, indent=4, ensure_ascii=False)
#------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    check_tasks_file_absent()






