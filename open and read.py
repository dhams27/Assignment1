# Task 1: Read a File and Handle Errors

try:
    print("Reading file content:\n")
    with open("output.txt", "rt") as fh:
        lines = fh.readlines()

        # Print each line with line numbers
        for index, line in enumerate(lines, start=1):
            print(f"Line {index}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
