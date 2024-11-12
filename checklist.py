# Populates a checklist for each employee with a month's worth of tasks
# Randomly assigns tasks to each employee based on weighting, frequency, and 

import random
import math
import json
from datetime import datetime
employee_data = json.load(open("employee_data.json"))
employee_list = list(employee_data.keys())
checklist = {}
checklist_data = json.load(open("checklist_data.json"))


def update_employee_data(ID):
    # Updates employee data with what tasks were done and when they were done
    for task in employee_data[ID]["tasks"]:
        if task["completed"]:
            task["completed_date"] = datetime.now().strftime("%m/%d/%Y")
        else:
            task["completed_date"] = ""


class Task:
    def __init__(self, name, frequency, shift, weighting):
        self.name = name
        self.frequency = frequency  # How often task needs to be done - value between 0 and 7, 7 meaning daily, .25 meaning once every 4 weeks
        self.shift = shift  # Need to assign keywords to shifts still
        self.weighting = weighting  # Difficulty weighting
        self.completed = False
        self.completed_date = ""
    def distribute_tasks(self):
        # Track task weights per employee to balance workload
        employee_weights = {employee: 0 for employee in employee_list}
        
        # Get task undesirability score from checklist data
        task_undesirability = next(
            (task["undesirability"] for task in checklist_data["tasks"] if task["taskName"] == self.name), 0
        )
        
        # Distribute tasks based on frequency and employee workload
        for employee, weight in employee_weights.items():
            if random.random() >= self.frequency:
                continue
                
            # Weight factor decreases as employee gets more undesirable tasks    
            if random.random() < 1 / (1 + weight):
                self.assign_task(employee)
                employee_weights[employee] += task_undesirability


    def assign_task(self, employee):
        if employee in checklist:
            checklist[employee].append(self)
        else:
            checklist[employee] = [self]



def main():
    for ID in employee_list:
        update_employee_data(ID)

main()
