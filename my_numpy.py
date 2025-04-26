import my_numpy as np

# Create an array with numbers from 10 to 50
arr = np.arange(10, 51)

# Find the maximum and minimum values
max_val = np.max(arr)
min_val = np.min(arr)

# Multiply all elements by 3
multiplied_arr = arr * 3

# Output the results
print("Original Array:\n", arr)
print("Maximum Value:", max_val)
print("Minimum Value:", min_val)
print("Array after multiplying by 3:\n", multiplied_arr)
