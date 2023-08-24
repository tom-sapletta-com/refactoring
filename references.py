import os
import csv
import argparse
import json

# Python script that searches for files recursively in a directory, checks the filenames in each file, and outputs the results in a CSV file format:
# example: ./references.py ./ references.csv


def list_filenames(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            # Exclude hidden files
            if not file.startswith('.') and not file.startswith('.md') and len(file) > 1:
                filepath = os.path.join(root, file)
                result.append({file:filepath})
    return result
    
def check_filenames(directory):
    result = []
    for item in list_filenames(directory):
        for filename, filepath in item.items():
            result[filepath] = []

        
    for item2 in list_filenames(directory):
        for filename, filepath in item2.items():
            for item1 in list_filenames(directory):
                for content_filename, content_filepath in item1.items():                
                    with open(content_filename, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if filename in content:  
                            print(file + 'added')
                            result[content_filepath].append(filename)
    return result


def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File'])
        writer.writerows([[file] for file in data])


def write_to_json(data, output_file):
    with open(output_file, 'w', newline='') as f:
        json.dump(data, f)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check dependencies in files.')
    parser.add_argument('directory', type=str, help='The directory to search in')
    parser.add_argument('output_file', type=str, help='The output CSV file name')
    args = parser.parse_args()

    directory_to_search = args.directory
    output_file = args.output_file

    result = check_filenames(directory_to_search)
    write_to_csv(result, output_file)
    write_to_json(result, output_file)
