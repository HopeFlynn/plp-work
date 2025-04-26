import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 19],
    'Grade': [75, 45, 60]
}

df = pd.DataFrame(data)

# Step 2: Add a "Passed" column (True if Grade > 50)
df['Passed'] = df['Grade'] > 50

# Step 3: Filter students who passed
passed_students = df[df['Passed'] == True]

# Display the DataFrame
print("All Students:\n", df)
print("\nStudents Who Passed:\n", passed_students)
