#!/usr/bin/python3
'''module: 0-gather_data_from_an_API
'''

import json
import requests
import sys

if __name__ == '__main__':

    root = 'https://jsonplaceholder.typicode.com'
    id_str = sys.argv[1]
    user_id = int(id_str)
    user = requests.get(root + "/users?userId=" + id_str).json()
    employee_name = user[0].get('name')

    todo_list = requests.get(root + "/todos?userId=" + id_str).json()
    total_todos = len(todo_list)
    completed_todos = 0
    for todo in todo_list:
        if todo.get('completed'):
            completed_todos += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          completed_todos, total_todos))
    for task in todo_list:
        if task.get('completed'):
            print("\t " + task['title'])
