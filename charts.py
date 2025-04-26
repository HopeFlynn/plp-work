import matplotlib.pyplot as plt

# === 1. Bar Chart – Population by Country ===
countries = ['Kenya', 'USA', 'India', 'Germany', 'Brazil']
population = [54, 331, 1390, 83, 213]  # in millions

plt.figure(figsize=(12, 4))  # Wide layout for side-by-side plots
plt.subplot(1, 3, 1)
plt.bar(countries, population, color='skyblue')
plt.title("Population of Countries")
plt.xlabel("Country")
plt.ylabel("Population (millions)")

# === 2. Pie Chart – Student's Daily Schedule ===
activities = ['Sleep', 'Study', 'Classes', 'Leisure', 'Meals', 'Chores']
hours = [8, 4, 5, 3, 2, 2]

plt.subplot(1, 3, 2)
plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
plt.title("Student's 24hr Time Use")
plt.axis('equal')

# === 3. Line Chart – Temperature Throughout the Day ===
times = ['Morning', 'Noon', 'Evening', 'Night']
temperatures = [18, 28, 24, 16]

plt.subplot(1, 3, 3)
plt.plot(times, temperatures, marker='o', linestyle='-', color='tomato')
plt.title("Temperature Changes")
plt.xlabel("Time of Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.tight_layout()
plt.show()
