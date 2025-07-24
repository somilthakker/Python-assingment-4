# task1_read_file.py

file_name = "sample.txt"

try:
    with open(file_name, 'r') as file:
        print("Reading file content:")
        for idx, line in enumerate(file, start=1):
            print(f"Line {idx}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file `{file_name}` was not found.")
