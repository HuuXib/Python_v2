import pandas as pd

xlsx_file = 'korelacja.xlsx'
df = pd.read_excel(xlsx_file, engine='openpyxl')

df = df.dropna(axis=0, how='all')  # usuwa puste wiersze
df = df.dropna(axis=1, how='all')  # usuwa puste kolumny

csv_file = 'korelacja_converted.csv'
df.to_csv(csv_file, index=False)    
