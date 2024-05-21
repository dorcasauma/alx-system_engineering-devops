#!/usr/bin/python3

"""
Script to fetch and display TODO list progress for a given employee ID using a REST API.

Requirements:
- Uses urllib or requests module
- Accepts an integer as a parameter, which is the employee ID
- Displays employee TODO list progress in a specific format
"""

import requests
import sys

def get_employee_name(employee_id):
    """
    Fetches and returns the name of the employee with the given ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    user_data = response.json()
    return user_data['name']

def get_todo_list(employee_id):
    """
    Fetches and returns the TODO list of the employee with the given ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of TODO items.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


