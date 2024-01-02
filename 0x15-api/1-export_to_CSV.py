#!/usr/bin/python3
"""
This script exports TODO list data for a given employee ID to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    # Extract employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Fetching user data
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    ).json()

    # Fetching TODO list
    todo_data = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id
            )).json()


    # Creating CSV file
    csv_filename = '{}.csv'.format(employee_id)

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Writing header
        csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                )

        # Check the retrieved TODO data
        print("TODO data:", todo_data)
        # Writing tasks
        for task in todo_data:
            csv_writer.writerow([
                user_data['id'],
                user_data['username'],
                str(task['completed']),
                task['title']
            ])

    # Print a message indicating successful data export
    print("Data exported to {}".format(csv_filename))
