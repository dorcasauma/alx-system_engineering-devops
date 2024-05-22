#!/usr/bin/python3

"""
This script uses the REST API from JSONPlaceholder to fetch and display
the TODO list progress of a given employee ID.
"""

import requests
import sys


def get_user_data(employee_id):

    """
    Fetches the name of the employee with the given ID from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    user_data = response.json()
    return user_data


def get_todo_list(employee_id):
    """
    Fetches the TODO list of the employee with the given ID from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of todos.
    """
    url = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={'userId': employee_id})
    response.raise_for_status()
    todo_list = response.json()
    return todo_list


def completed_tasks(todo_list):
    """
    Counts the number of completed tasks in the TODO list.

    Args:
        todo_list (list): The list of TODO items.

    Returns:
        int: The number of completed tasks.
    """
    done_tasks = 0
    for task in todo_list:
        if task['completed']:
            done_tasks +=1
    return done_tasks


if __name__ == "__main__":
    employeeId = int(sys.argv[1])
    user_data = get_user_data(employeeId)
    employee_name = user_data["name"]
    todo_list = get_todo_list(employeeId)
    total_tasks = len(todo_list)
    done_tasks = completed_tasks(todo_list)
    print(f"Employee {employee_name} is done with tasks("
        f"{done_tasks}/{total_tasks}):")
    for task in todo_list:
        if task['completed']:
            print(f"\t {task['title']}")
