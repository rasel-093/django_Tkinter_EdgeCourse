import pandas as pd
dataframe = pd.read_csv('heart.csv')
# Shape of dataset
print(dataframe.shape)

# Print first 5 record
# print(dataframe.head())

# print(dataframe.isnull().any)
# Better to convert string to numeric value: say male = 0, female = 1
# print(dataframe.nunique())