import json
def convert_shifts_to_json():
	shifts = []
	
	with open('shift_weights.txt', 'r') as file:
		# Skip header line
		next(file)
	
		for line in file:
			if line.strip() == '': #Skip empty lines
				continue
			#Split line by comma
			parts = line.strip().split(',')
			shift = {
				"start": parts[0].strip(),
				"end": parts[1].strip(),
				"weekday": parts[2].strip(),
				"location": parts[3].strip(),
				"weighting": parts[4].strip(),
			}
			shifts.append(shift)
	json_data = {"shifts": shifts}
	with open('shift_weights.json', 'w') as json_file:
		json.dump(json_data, json_file, indent = 4)

if __name__ == "__main__":
	convert_shifts_to_json()
