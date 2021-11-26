import pandas as pd
target = r'..\data\allExport.csv'
print("Loading data...")
print(f"Storing data to {target}")
pd.read_csv('https://github.com/ftmnl/asr/raw/main/data/allExport.csv', sep='|').to_csv(target, index=False)  # noqa: E501
print("Done!")
