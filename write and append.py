# Task 2: Write and Append Data to a File

try:
    # Step 1: Write initial input to file
    text = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(text + "\n")
    print("Data successfully written to output.txt.\n")

    # Step 2: Append additional data
    additional_text = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write(additional_text + "\n")
    print("Data successfully appended.\n")

    # Step 3: Read and display final content
    print("Final content of output.txt:")
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
