#!/usr/bin/python3
'''module: 0-gather_data_from_an_API
'''

import json
import requests
import sys

if __name__ == '__main__':

    root = 'https://jsonplaceholder.typicode.com'
    user_id = int(sys.argv[1])
    user_list = requests.get(root + "/users/").json()

    for index, user in enumerate(user_list):
        if user.get('id') == user_id:
            employee_name = user.get('name')
            employee_index = index
            break

    todo_list = requests.get(root + "/todos/").json()
    total_todos = 0
    completed_todos = 0
    employee_tasks = []
    for todo in todo_list:
        if todo.get('userId') == user_id:
            total_todos += 1
            if todo.get('completed'):
                employee_tasks.append(todo.get('title'))
                completed_todos += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          completed_todos, total_todos))
    for task in employee_tasks:
        print("\t " + task)
