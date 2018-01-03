#!/usr/bin/python3
'''module: 3-dictionary_of_list_of_dictionaries
builds a dict of users and each user has a list of tasks as a value
based on api. then outputs to json format file
output: json file: todo_all_employees.json
'''

import json
import requests

if __name__ == '__main__':

    root = 'https://jsonplaceholder.typicode.com'
    # user_id = int(id_str)
    tmp_users = requests.get(root + "/users/").json()
    users = {str(user.get('id')): user.get('username') for user in tmp_users}
    # print("===================== users =============================")
    # print(users)

    user_tasks = {}

    for key in sorted(users.keys()):
        user_name = users.get(key)

        todo_list = requests.get(root + "/todos?userId=" + key).json()

        for todo in todo_list:
            del todo['id']
            del todo['userId']
            todo['task'] = todo['title']
            del todo['title']
            todo['username'] = user_name

        user_tasks[key] = todo_list

    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as outfile:
        json.dump(user_tasks, outfile)
