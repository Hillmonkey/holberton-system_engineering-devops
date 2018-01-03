#!/usr/bin/python3
'''module: 2-export_to_JSON
accepts: user_id from command line
output: json file name: <user_id>.json
'''

import json
import requests
import sys

if __name__ == '__main__':

    root = 'https://jsonplaceholder.typicode.com'
    id_str = sys.argv[1]
    user_id = int(id_str)
    user = requests.get(root + "/users?userId=" + id_str).json()
    user_name = user[0].get('username')

    todo_list = requests.get(root + "/todos?userId=" + id_str).json()

    for todo in todo_list:
        del todo['id']
        del todo['userId']
        todo['task'] = todo['title']
        del todo['title']
        todo['username'] = user_name

    user_tasks = {}
    user_tasks[id_str] = todo_list

    json_file = id_str + ".json"
    with open(json_file, 'w') as outfile:
        json.dump(user_tasks, outfile)
