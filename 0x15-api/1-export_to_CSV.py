#!/usr/bin/python3
'''module: 1-export_to_CSV
accepts: one command line argument: user_id
outputs: csv file in this format: <user_id>.csv
'''

import csv
import json
import requests
import sys

if __name__ == '__main__':

    root = 'https://jsonplaceholder.typicode.com'
    id_str = sys.argv[1]
    user_id = int(id_str)
    fname = id_str + ".csv"
    user_list = requests.get(root + "/users/").json()

    for index, user in enumerate(user_list):
        if user.get('id') == user_id:
            employee_name = user.get('name')
            user_name = user.get('username')
            employee_index = index
            break

    todo_list = requests.get(root + "/todos/").json()
    total_todos = 0
    completed_todos = 0
    employee_tasks = []
    for todo in todo_list:
        if todo.get('userId') == user_id:
            employee_tasks.append((todo.get('title'),
                                   todo.get('completed')))

    with open(fname, 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_ALL)
        for task in employee_tasks:
            task_writer.writerow([id_str, user_name, task[1], task[0]])
