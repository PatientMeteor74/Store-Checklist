import json

def convert_txt_to_json():
    tasks = []
    
    with open('checklist_data.txt', 'r') as file:
        # Skip the header line
        next(file)
        
        for line in file:
            if line.strip() == '':  # Skip empty lines
                continue
            
            # Split the line by comma, but not within curly braces
            parts = line.split(',', 4)  # Split into 5 parts
            
            # Extract shift information
            shift_str = parts[3].strip()
            shift_dict = {}
            
            # Parse the shift information
            if '{' in shift_str:
                shift_parts = shift_str.replace('{', '').replace('}', '').split(',')
                for part in shift_parts:
                    if ':' in part:
                        key, value = part.split(':')
                        key = key.strip().lower()
                        value = value.strip().strip('"')
                        shift_dict[key] = value
            
            task = {
                "taskName": parts[0].strip(),
                "undesirability": int(parts[1].strip()),
                "frequencyPerWeek": float(parts[2].strip()),
                "shift": {
                    "weekday": shift_dict.get('weekday', '').strip(),
                    "times": shift_dict.get('times', '').strip(),
                    "location": shift_dict.get('location', '').strip()
                },
                "description": parts[4].strip()
            }
            tasks.append(task)
    
    # Create the final JSON structure
    json_data = {"tasks": tasks}
    
    # Write to JSON file with proper indentation
    with open('checklist_data.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    convert_txt_to_json()