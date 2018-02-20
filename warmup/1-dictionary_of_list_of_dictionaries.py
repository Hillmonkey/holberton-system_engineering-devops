#!/usr/bin/python3

'''module: 1-dictionary_of_list_of_dictionaries
'''

if __name__ == "__main__":

    import json
    from pprint import pprint
    import requests

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_xx = requests.get('https://jsonplaceholder.typicode.com/users').json()

    users = {}
    for user in user_xx:
        users[str(user["id"])] = user["username"]
    # print(users)
    # print()

    todo_dict = {}

    for i, todo in enumerate(todos):
        if str(todo["userId"]) not in todo_dict:
            todo_dict[str(todo["userId"])] = []
            # print(todo["userId"])
        little_dict = {}
        little_dict['username'] = users[str(todo['userId'])]
        little_dict['task'] = todo['title']
        little_dict['completed'] = todo['completed']

        todo_dict[str(todo['userId'])].append(little_dict)

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(todo_dict, outfile)
    # pprint(todo_dict)
