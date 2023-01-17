#!/usr/bin/python3
'''
Script that uses a given REST API for a given employee ID
and returns information about his/her TODO list progress
and export it in the JSON format
'''
import json
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    employeeDict = {employeeId: []}
    for task in tasks:
        employeeDict[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeId), 'w') as f:
        json.dump(employeeDict, f)
