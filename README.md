# Real Estate Analysis: 2D Arrays & Pandas

A Python script that takes real estate data stored as a raw 2D array, converts it into a Pandas DataFrame, computes total market values through vectorized operations, sorts the result in descending order, and renders a bar chart with Matplotlib. The first step into the world of high-level languages, revisiting the classic pain point of sorting a 2D array, now done the Python way.

---

## What This Project Demonstrates

- Working with raw 2D arrays (nested lists) as a data source
- Converting a 2D array into a structured Pandas DataFrame with named columns
- Vectorized column operations that is, computing derived values without loops
- Sorting a DataFrame by a calculated column in descending order
- Basic data visualization with Matplotlib using a bar chart
- The conceptual bridge from low-level array sorting to high-level library driven data manipulation

---

## Project Structure

```
2D_ARRAY/
└── 2D_ARRAY.py    # Full pipeline: data → DataFrame → sort → visualize
```

---

## The Data

The dataset is defined as a plain Python list of lists, each row represents a real estate area:

```python
data = [
    ["Downtown",   15000, 120],
    ["Suburbs",     5000, 250],
    ["Midtown",     8000, 180],
    ["Waterfront", 22000,  95],
    ["Old Town",    6500, 300]
]
```

| Column         | Description                   |
|----------------|-------------------------------|
| `Area_Name`    | Name of the area              |
| `Price_Per_SQM`| Price per square metre (€)    |
| `Total_Size`   | Total property size (m²)      |

---

## Pipeline

**Step 1: Convert to DataFrame:**
```python
columns = ['Area_Name', 'Price_Per_SQM', 'Total_Size']
df = pd.DataFrame(data, columns=columns)
```

**Step 2: Calculate Total Value (vectorized):**
```python
df['Total_Value'] = df['Price_Per_SQM'] * df['Total_Size']
```
No loops. Pandas multiplies the entire column at once.

**Step 3: Sort descending:**
```python
df_sorted = df.sort_values(by='Total_Value', ascending=False)
```

**Step 4: Visualize:**
```python
plt.bar(df_sorted['Area_Name'], df_sorted['Total_Value'], color='skyblue')
plt.show()
```

---

## Dependencies

```bash
pip install pandas matplotlib
```

---

## Running the Script

```bash
python 2D_ARRAY.py
```

The script prints the sorted DataFrame to the terminal and opens a Matplotlib bar chart window showing Total Market Value by Area.

---

## Notes

This project intentionally keeps the data inline rather than loading from a CSV or database. The point is to show the conversion from a raw 2D structure into a DataFrame clearly and directly. The sorting logic is the same problem solved in lower-level languages during early CS coursework, now expressed in two lines with Pandas.

---

## Author

**Dimitrios Dalaklidis** — CS student at the University of Western Macedonia, interested in backend development, systems programming, and cloud infrastructure.  
📧 dalaklidesdemetres@gmail.com
