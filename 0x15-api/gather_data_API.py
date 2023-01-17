#!/usr/bin/python3
'''
Script that uses a given REST API for a given employee ID
and returns information about his/her TODO list progress
'''
import requests
import sys


if __name__ == "__main__":
    # Creating employee ID as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py [employee_id]")
        sys.exit()
    employee_id = sys.argv[1]

    # Creating a GET request to the API
    url = "https://jsonplaceholder.typicode.com/todos/{}".format(employee_id)
    res = requests.get(url)

    # Extracting the employee name and task information from the API response
    employee_name = ""
    number_of_done_tasks = []
    total_number_of_tasks = 0
    if res.status_code == 200:
        data = res.json()
        total_number_of_tasks = len(data)
        for task in data:
            if task["completed"]:
                number_of_done_tasks.append(task["title"])
            if employee_name == "":
                user_url = "https://jsonplaceholder.typicode.com/users/{}"\
                            .format(employee_id)
                user_res = requests.get(user_url)
                if user_res.status_code == 200:
                    employee_name = user_res.json()["name"]
    else:
        print("Error: Unable to retrieve employee data.")
        sys.exit()

    # Display employee information in a specific format
    print(f"Employee {employee_name} is done with\
          tasks({len(number_of_done_tasks)}/{total_number_of_tasks}): ")
    for task in number_of_done_tasks:
        print("\t {}".format(task))
