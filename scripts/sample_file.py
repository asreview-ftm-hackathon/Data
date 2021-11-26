# import pandas
import pandas as pd

# Load the data
print("Loading data...")
df = pd.read_csv(r'..\data\allExport.csv')

# scramble the data
print("Scrambling data...")
df = df.sample(frac=1).reset_index(drop=True)

# split dataset into 10 different files
print("Splitting data...")
df_list = [df[i::10] for i in range(10)]

# save df_list to 10 different files
print("Saving data...")
for i in range(10):
    df_list[i].to_excel(f'..\\sampled data\\preprocessed_{i+1}.xlsx',
                        index=False)
