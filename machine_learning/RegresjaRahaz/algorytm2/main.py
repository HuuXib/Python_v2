import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import preprocessing


korelacja_df = pd.read_excel('korelacja.xlsx')

# korelacja_df['przystanek wejściowy'] = pd.to_datetime(korelacja_df['przystanek wejściowy'], format='%H:%M', errors='coerce')
# korelacja_df['przystanek wyjściowy'] = pd.to_datetime(korelacja_df['przystanek wyjściowy'], format='%H:%M', errors='coerce')

korelacja_df['HH:MM'] = pd.to_datetime(korelacja_df['HH:MM'])
korelacja_df = korelacja_df.dropna(axis=0, how='all')  # usuwa puste wiersze
korelacja_df = korelacja_df.dropna(axis=1, how='all')  # usuwa puste kolumny



print(korelacja_df.head(10))
print(korelacja_df.dtypes)


korelacja_df['roznica(min)'] = (
    (korelacja_df['przystanek wyjściowy'] - korelacja_df['przystanek wejściowy'])
    .dt.total_seconds() / 60
)
print(korelacja_df)