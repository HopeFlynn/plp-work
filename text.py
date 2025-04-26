# Step 1: Create the input file with some sample content
with open("input.txt", "w") as file:
    file.write("Learning Python is fun!\n")
    file.write("This is a great way to start coding.\n")
    file.write("Practice makes perfect.\n")
    file.write("Functions and loops are powerful.\n")
    file.write("Keep building projects!\n")

# Step 2: Read from input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 3: Count the number of words
word_count = len(content.split())

# Step 4: Convert all text to uppercase
uppercase_content = content.upper()

# Step 5: Write to output.txt
with open("output.txt", "w") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(uppercase_content + "\n")
    file.write(f"WORD COUNT: {word_count}\n")

# Step 6: Print a success message
print("✅ output.txt created successfully with processed content and word count!")
