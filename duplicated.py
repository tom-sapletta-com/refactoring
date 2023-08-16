import os
import csv

# recursively traverses a directory, searches for files, and checks the filenames in each file. It then lists the results in a CSV file format:

def check_filenames(directory):
    result = []
    for root, _, files in os.walk(directory):
        for file in files:
            filename = os.path.join(root, file)
            with open(filename, 'r') as f:
                content = f.read()
                if 'example' in content:  # Replace 'example' with the filename condition you want to check
                    result.append(filename)
    return result

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File'])
        writer.writerows([[file] for file in data])
