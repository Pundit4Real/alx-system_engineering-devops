#!/usr/bin/python3
'''
Script that uses a given REST API for a given employee ID
and returns information about his/her TODO list progress
'''
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    totalNumberOfTasks = 0
    numberOfDoneTasks = []

    for task in tasks:
        if task.get('completed'):
            numberOfDoneTasks.append(task)
            totalNumberOfTasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, totalNumberOfTasks, len(tasks)))

    for task in numberOfDoneTasks:
        print("\t {}".format(task.get('title')))
