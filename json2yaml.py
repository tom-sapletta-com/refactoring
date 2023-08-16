import argparse
import json
import yaml

# Python script that converts a JSON file to YAML format:

def convert_json_to_yaml(json_file, yaml_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    with open(yaml_file, 'w') as f:
        yaml.dump(data, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert JSON file to YAML format.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file')
    parser.add_argument('yaml_file', type=str, help='Path to the output YAML file')
    args = parser.parse_args()

    json_file_path = args.json_file
    yaml_file_path = args.yaml_file

    convert_json_to_yaml(json_file_path, yaml_file_path)
