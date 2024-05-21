#!/usr/bin/python3
import requests
import sys



def get_employee_name(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    user_data = response.json
    return user_data["name"]

def get_todo_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={'userId': employee_id})
    response.raise_for_status()
    return response.json()