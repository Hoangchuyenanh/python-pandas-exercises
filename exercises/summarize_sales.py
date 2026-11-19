from pathlib import Path

import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
data_path = project_dir / "data" / "sample_sales.csv"

sales = pd.read_csv(data_path)
summary = sales.groupby("category")["amount"].sum()

print("Total sales by category:")
print(summary)