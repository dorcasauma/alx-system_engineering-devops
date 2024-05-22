#!/usr/bin/python3


"""
This script fetches tasks for all users from the JSONPlaceholder API
and exports the data to a JSON file.
"""


import json
import requests


def fetch_all_tasks():
    """
    Fetch tasks for all users from the JSONPlaceholder API.

    Returns:
        dict: Dictionary containing tasks for all users.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code == 200:
        tasks = response.json()
        tasks_by_user = {}
        for task in tasks:
            user_id = task.get('userId')
            if user_id not in tasks_by_user:
                tasks_by_user[user_id] = []
            tasks_by_user[user_id].append({
                "username": task.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            })
        return tasks_by_user


def export_to_json(data):
    """
    Export tasks data to a JSON file.

    Args:
        data (dict): Dictionary containing tasks for all users.

    Returns:
        None
    """
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == "__main__":
    tasks_by_user = fetch_all_tasks()
    if tasks_by_user:
        export_to_json(tasks_by_user)

