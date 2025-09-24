import pandas as pd

xlsx_file = 'tabela brak przesiadek.xlsx'
df = pd.read_excel(xlsx_file, engine='openpyxl')


csv_file = 'przesiadki.csv'
df.dropna(axis=1, how='all').to_csv('output.csv', index=False)