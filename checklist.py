# Populates a checklist for each employee with a month's worth of tasks
# Randomly assigns tasks to each employee based on weighting, frequency, and 

import random
import math
import json
from datetime import datetime
employee_data = json.load(open("employee_data.json"))
employee_list = list(employee_data.keys())

def update_employee_data(ID):
    # Updates employee data with what tasks were done and when they were done
    for task in employee_data[ID]["tasks"]:
        if task["completed"]:
            task["completed_date"] = datetime.now().strftime("%m/%d/%Y")
        else:
            task["completed_date"] = ""



def main():
    for ID in employee_list:
        update_employee_data(ID)

main()
