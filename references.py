import os
import csv
import argparse

# Python script that searches for files recursively in a directory, checks the filenames in each file, and outputs the results in a CSV file format:
# example: ./references.py ./ references.csv

def check_filenames(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            # Exclude hidden files
            if not file.startswith('.'):
                filename = os.path.join(root, file)
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if file in content:  
                        print(file + 'added')
                        result.append(filename)
    return result

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File'])
        writer.writerows([[file] for file in data])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check dependencies in files.')
    parser.add_argument('directory', type=str, help='The directory to search in')
    parser.add_argument('output_file', type=str, help='The output CSV file name')
    args = parser.parse_args()

    directory_to_search = args.directory
    output_file = args.output_file

    result = check_filenames(directory_to_search)
    write_to_csv(result, output_file)
