import os

file_path = "example.txt"

with open(file_path, "r") as file:

    lines = file.readlines()

    num_lines = len(lines)

    print(f"The file contains {num_lines} lines.")

    print("File contents:\n")
    for line in lines:
        print(line.strip())