import json
import csv

def clean_json(file_path):
    # open the json path and load the data
    with open(file_path, 'r') as file:
        data = json.load(file)
    # clean the data, remove empty values and write to a csv file
    def remove_empty_values(d):
        if isinstance(d, dict):
            return {k: remove_empty_values(v) for k, v in d.items() if v not in [None, ""]}
        elif isinstance(d, list):
            return [remove_empty_values(i) for i in d if i not in [None, ""]]
        else:
            return d
    cleaned_data = remove_empty_values(data)
    # Write cleaned data to a CSV file
    csv_file_path = file_path.replace('.json', '.csv')
    with open(csv_file_path, 'w', newline='') as csv_file:
        if isinstance(cleaned_data, list) and len(cleaned_data) > 0:
            keys = cleaned_data[0].keys()
            dict_writer = csv.DictWriter(csv_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(cleaned_data)

# Example usage
clean_json('Test.json')