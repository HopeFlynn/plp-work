# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# 1. NumPy: Create array and calculate mean
numbers = np.arange(1, 11)  # Numbers from 1 to 10
mean_value = np.mean(numbers)
print("Mean of numbers 1 to 10:", mean_value)

# 2. Pandas: Load small dataset and display summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Grade': [88, 75, 90]
}
df = pd.DataFrame(data)
print("\nSummary statistics:\n", df.describe())

# 3. Requests: Fetch data from a public API
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
if response.status_code == 200:
    bitcoin_data = response.json()
    usd_rate = bitcoin_data['bpi']['USD']['rate']
    print("\nCurrent Bitcoin Price in USD:", usd_rate)
else:
    print("Failed to fetch data from API")

# 4. Matplotlib: Simple line graph
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y = X^2")
plt.grid(True)
plt.show()
