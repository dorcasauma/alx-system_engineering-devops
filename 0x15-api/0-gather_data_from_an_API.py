#!/usr/bin/python3
"""
This script uses the REST API from JSONPlaceholder to fetch and display
the TODO list progress of a given employee ID.
"""

import requests
import sys

def get_employee_name(employee_id):
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
    return user_data['name']

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
    return response.json()

def main(employee_id):
    """
    Main function to fetch and print the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    try:
        employee_name = get_employee_name(employee_id)
        todo_list = get_todo_list(employee_id)

        total_tasks = len(todo_list)
        done_tasks = [task for task in todo_list if task['completed']]
        number_of_done_tasks = len(done_tasks)

        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Invalid employee ID")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            main(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
