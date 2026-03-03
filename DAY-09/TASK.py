import pandas as pd
import matplotlib.pyplot as plt
dt = pd.read_csv("coffee_shop_sales.csv")
quantity_per_category = dt.groupby('product_category')['transaction_qty'].sum()
print(quantity_per_category)
plt.figure(figsize=(8,5))
plt.bar(quantity_per_category.index, quantity_per_category.values)
plt.xlabel("Product Category")
plt.ylabel("Total Quantity Sold")
plt.title("Total Quantity Sold per Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()