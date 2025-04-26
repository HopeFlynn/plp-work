import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# Calculate total revenue
total_revenue = df['Revenue ($)'].sum()

# Find the best-selling product
best_seller = df.groupby('Product')['Quantity Sold'].sum().idxmax()
best_seller_units = df.groupby('Product')['Quantity Sold'].sum().max()

# Identify the day with the highest sales
top_day = df.groupby('Date')['Revenue ($)'].sum().idxmax()
top_day_revenue = df.groupby('Date')['Revenue ($)'].sum().max()

# Save results to text file
with open('sales_summary.txt', 'w') as f:
    f.write(f"Total Revenue: ${total_revenue:,}\n")
    f.write(f"Best-Selling Product: {best_seller} ({best_seller_units} units sold)\n")
    f.write(f"Highest Sales Day: {top_day} (${top_day_revenue:,})\n")

# Print results nicely
print("🔍 Sales Summary:")
print(f"Total Revenue: ${total_revenue:,}")
print(f"Best-Selling Product: {best_seller} ({best_seller_units} units sold)")
print(f"Highest Sales Day: {top_day} (${top_day_revenue:,})")

# BONUS: Visualize sales trends
daily_sales = df.groupby('Date')['Revenue ($)'].sum()

plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', color='teal')
plt.title('📈 Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()
