# refactoring
Restructuring existing computer code with dedicated scripts


## references

To execute this script as a shell command with input parameters, follow these steps:

1. Save the script to a Python file (e.g., `references.py`).
2. Make the file executable by running `chmod +x references.py`.
3. Run the command with the desired input parameters like:

```bash
./references.py /path/to/directory output.csv
```



## duplicated files

```python
directory_to_search = '/path/to/directory'  # Replace with the directory you want to search in
output_file = 'output.csv'  # Replace with the desired output CSV file name

result = check_filenames(directory_to_search)
write_to_csv(result, output_file)
````


# file converter

To execute this script as a shell command with input parameters, follow these steps:

1. Save the script to a Python file (e.g., `json2yaml.py`).
2. Make the file executable by running `chmod +x json2yaml.py`.
3. Run the command with the desired input parameters like:

```bash
./json2yaml.py input.json output.yaml
```

Replace `input.json` with the path to your JSON file and `output.yaml` with the desired output YAML file path.

