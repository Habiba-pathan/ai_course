import pandas as pd
dt = pd.read_csv("coffee_shop_sales.csv")
dt["total_price"] = dt["transaction_qty"] * dt["unit_price"]
t_sales = 0
t_sales += dt["total_price"].sum()
print("Total sales: ",t_sales)
print(dt.head())
