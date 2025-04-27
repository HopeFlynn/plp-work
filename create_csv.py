import pandas as pd

# Sample data
data = {
    'Date': ['2025-03-01', '2025-03-01', '2025-03-02', '2025-03-02'],
    'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard'],
    'Quantity Sold': [5, 15, 3, 8],
    'Revenue ($)': [5000, 300, 3000, 800]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sales_data.csv', index=False)

print("✅ sales_data.csv created successfully!")
