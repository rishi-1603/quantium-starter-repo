import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df = df[df["product"] == "Pink Morsels"]

df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv("formatted_output.csv", index=False)

print("Output file created successfully")