# Ask user for a file name
filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()
    
    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("modified_output.txt", "w") as new_file:
        new_file.write(modified_content)

    print("✅ File read successfully and modified content saved to 'modified_output.txt'.")

except FileNotFoundError:
    print("❌ Error: The file was not found.")
except IOError:
    print("❌ Error: The file could not be read or written.")
