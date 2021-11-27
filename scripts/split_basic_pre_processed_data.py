import os
import pandas as pd

# Settings
num_samples = 10

# Load the data
print("Loading data...")
df = pd.read_csv(r'..\data\preprocessed_data.csv')

# scramble the data
print("Scrambling data...")
df = df.sample(frac=1).reset_index(drop=True)

# split dataset into num_samples different files
print(f"Splitting data into {num_samples} parts...")
df_list = [df[i::num_samples] for i in range(num_samples)]

# create a folder for the data if it doesn't exist
if not os.path.exists(r'..\split_preprocessed'):
    os.makedirs(r'..\split_preprocessed')

# save df_list to num_samples different files
print("Saving data...")
for i in range(num_samples):
    df_list[i].to_csv(f'..\\split_preprocessed\\preprocessed_{i+1}.csv',
                        index=False)
