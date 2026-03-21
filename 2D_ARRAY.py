import pandas as pd
import matplotlib.pyplot as plt

# 1. Your raw 2D array (The Data)
data = [
    ["Downtown", 15000, 120],
    ["Suburbs", 5000, 250],
    ["Midtown", 8000, 180],
    ["Waterfront", 22000, 95],
    ["Old Town", 6500, 300]
]

# 2. Converting to a Pandas DataFrame
columns = ['Area_Name', 'Price_Per_SQM', 'Total_Size']
df = pd.DataFrame(data, columns=columns)

# 3. Logic: Calculate Total_Value (Vectorized operation)
df['Total_Value'] = df['Price_Per_SQM'] * df['Total_Size']

# 4. Logic: Sort by Total_Value descending
df_sorted = df.sort_values(by='Total_Value', ascending=False)

# Display the result
print(df_sorted)

# 5. System Part: Visualization
plt.figure(figsize=(10, 6))
plt.bar(df_sorted['Area_Name'], df_sorted['Total_Value'], color='skyblue')
plt.xlabel('Area Name')
plt.ylabel('Total Market Value')
plt.title('Real Estate Analysis: Total Value by Area')
plt.show()