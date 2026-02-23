import pandas as pd

# Load dataset
df = pd.read_csv("orders.csv")

print("===== SUPPLY CHAIN ANALYSIS SYSTEM =====\n")

print("Dataset Loaded Successfully!\n")

print("First 5 Rows:")
print(df.head())

print("\nTotal Orders:", len(df))
print("Average Delivery Time:", df["delivery_days"].mean())
print("Total Revenue:", df["cost"].sum())

# Top selling product
top_product = df.groupby("product_id")["quantity"].sum().idxmax()
print("\nTop Selling Product ID:", top_product)

# Supplier with max delay
delay_supplier = df.groupby("supplier_id")["delivery_days"].mean().idxmax()
print("Supplier Causing Most Delay:", delay_supplier)

# Warehouse with highest orders
top_warehouse = df.groupby("warehouse_id")["quantity"].sum().idxmax()
print("Most Active Warehouse:", top_warehouse)

print("\nSystem Analysis Complete!")