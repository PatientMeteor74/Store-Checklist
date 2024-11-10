import json

def convert_employee_list_to_json():
    employees = []
    
    with open('employee_list.txt', 'r') as file:
        # Skip the header line and empty line
        next(file)
        next(file)
        
        for line in file:
            if line.strip() == '':  # Skip empty lines
                continue
                
            # Split the line by comma
            parts = line.strip().split(',', 3)  # Limit split to handle shifts
            
            # Handle shifts
            shifts = []
            if len(parts) > 3:
                shift_str = parts[3].strip()
                if shift_str != '[]':
                    # Extract shift data between { and }
                    shift_data = shift_str[2:-2]  # Remove [{ and }]
                    shift_parts = shift_data.split(',')
                    shift_dict = {}
                    for part in shift_parts:
                        if ':' in part:
                            key, value = part.split(':')
                            key = key.strip()
                            value = value.strip().strip('"')
                            shift_dict[key] = value
                    shifts.append(shift_dict)
            
            employee = {
                "lastName": parts[0].strip(),
                "firstName": parts[1].strip(),
                "employeeId": parts[2].strip(),
                "shifts": shifts
            }
            employees.append(employee)
    
    # Create the final JSON structure
    json_data = {"employees": employees}
    
    # Write to JSON file with proper indentation
    with open('employee_list.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    convert_employee_list_to_json()