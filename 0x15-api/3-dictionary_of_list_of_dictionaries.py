#!/usr/bin/python3
"""
This script exports TODO list data for all employees to a JSON file.
"""
import json
import requests


if __name__ == "__main__":
    # Fetching all users
    all_users = requests.get(

        'https://jsonplaceholder.typicode.com/users'
        ).json()

    # Creating dictionary to store data for all employees
    all_data = {}

    for user in all_users:
        # Fetching TODO list for each user
        todo_data = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user['id'])
        ).json()

        # Creating list of dictionaries for each user
        user_data_list = [
            {"username": user['username'],
             "task": task['title'],
             "completed": task['completed']
             } for task in todo_data
            ]

        # Adding the list to the dictionary with the user ID as the key
        all_data[user['id']] = user_data_list

    # Creating JSON file
    json_filename = 'todo_all_employees.json'

    with open(json_filename, 'w') as json_file:
        json.dump(all_data, json_file)

    print("Data exported to {}".format(json_filename))
