import pandas as pd

data = pd.read_csv('data.csv')
print(f"Number of columns in file are: {len(data)}")
print(data.head())
