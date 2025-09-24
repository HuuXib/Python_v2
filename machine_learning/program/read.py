import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import plotly.express as px
import seaborn as sns
from datetime import datetime, time



przesiadki_df = pd.read_csv('output.csv')


# przesiadki_df.info()

# przesiadki_df.describe()

sns.set_style('darkgrid')


przesiadki_df['godzina \nwejścia'] = pd.to_datetime(przesiadki_df['godzina \nwejścia'], format='%H:%M:%S')
przesiadki_df['godzina \nwyjścia'] = pd.to_datetime(przesiadki_df['godzina \nwyjścia'], format='%H:%M:%S')


start_hour = datetime.time(pd.to_datetime(input('Podaj początkową godzinę (FORMAT: H:M:S): ')))
end_hour = datetime.time(pd.to_datetime(input('Podaj koncową godzinę (FORMAT: H:M:S): ')))



start_range = pd.to_datetime(start_hour, format='%H:%M:%S')
end_range = pd.to_datetime(end_hour, format='%H:%M:%S')

filtered_df = przesiadki_df[(przesiadki_df['godzina \nwejścia'] >= start_range) & (przesiadki_df['godzina \nwyjścia'] <= end_range)]

print(filtered_df)



matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10,6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

fig = px.histogram(filtered_df, 
                   x = 'linia - kierunek',
                   marginal='box',
                   color_discrete_sequence=['red','blue'],
                   nbins=47,
                   title = f'Ruch między {datetime.time(start_range)} a {datetime.time(end_range)}')

fig.update_layout(bargap=0.1)
fig.show()



