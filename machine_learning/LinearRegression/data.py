import pandas as pd

medical_df = pd.read_csv('medical.csv')
medical_df
medical_df.info() # give us information about column types etc.
print(medical_df.describe()) # give us some information about data in our csv

