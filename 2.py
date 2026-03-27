import pandas as pd
df = pd.read_csv("data.csv")
sorted_df = df.sort_values(by="Name",ascending=True)
print("Sorted Data:\n", sorted_df)
print("\nFirst 3 rows:\n", df[:3])
print("\nSelected Columns:\n", df[["Name", "Marks"]])