
---

## 🧠 Python Code – `sales_analysis.py`

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display basic info
print("Dataset Overview:")
print(df.info())

# Total revenue by sales channel
channel_revenue = df.groupby("Sales_Channel")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Sales Channel:")
print(channel_revenue)

# Plot revenue by channel
plt.figure()
channel_revenue.plot(kind="bar")
plt.title("Revenue by Sales Channel")
plt.xlabel("Sales Channel")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# Monthly sales trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_trend = df.groupby("Month")["Revenue"].sum()

plt.figure()
monthly_trend.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Region-wise channel performance
region_channel = df.pivot_table(
    values="Revenue",
    index="Region",
    columns="Sales_Channel",
    aggfunc="sum"
)

print("\nRegion-wise Channel Performance:")
print(region_channel)

# Heatmap for better visualization
plt.figure()
sns.heatmap(region_channel, annot=True, fmt=".0f", cmap="Blues")
plt.title("Revenue Heatmap: Region vs Sales Channel")
plt.tight_layout()
plt.show()
