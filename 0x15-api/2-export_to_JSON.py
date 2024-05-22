#!/usr/bin/python3

"""
This script fetches tasks for a specified user ID from the JSONPlaceholder API
and exports the data to a JSON file.
"""

import json
import sys
import requests


def export_to_json(user_id, username, tasks):
    """
    Export tasks data to a JSON file.

    Args:
        user_id (int): The user ID.
        username (str): The username.
        tasks (list): List of tasks.

    Returns:
        None
    """
    data = {str(user_id): [{"task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": username} for task in tasks]}
    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)


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
        # Assuming the username is the same for all tasks
        username = tasks[0].get('username')
        export_to_json(user_id, username, tasks)
