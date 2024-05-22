#!/usr/bin/python3


"""
This script fetches tasks for a specified user ID from the JSONPlaceholder API
and exports the data to a CSV file.
"""


import csv
import requests
import sys


def export_to_csv(user_id, username, tasks):
    """
    Export tasks data to a CSV file.

    Args:
        user_id (int): The user ID.
        username (str): The username.
        tasks (list): List of tasks.

    Returns:
        None
    """
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def fetch_tasks(user_id):
    """
    Fetch tasks for the specified user ID from the JSONPlaceholder API.

    Args:
        user_id (int): The user ID.

    Returns:
        list: List of tasks.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


if __name__ == "__main__":

    user_id = int(sys.argv[1])
    tasks = fetch_tasks(user_id)
    if tasks:
        username = tasks[0].get('username')
        export_to_csv(user_id, username, tasks)
