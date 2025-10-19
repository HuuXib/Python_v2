import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import preprocessing

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10,6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
#Y - liczba pasazerow
#X - dzien tygodnia

passengers_df = pd.read_csv('regersja_liniowa_converted.csv')
#passengers and day
fig_data = px.histogram(passengers_df,
                        x = 'data',
                        marginal= 'box',
                        color_discrete_sequence=['blue'],
                        nbins=47
                        )
# fig_data.update_layout(bargap=0.1)
# fig_data.show()

passengers_df['data'] = pd.to_datetime(passengers_df['data'])

passengers_df['dzien_tygodnia'] = passengers_df['data'].dt.dayofweek






def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))


passengers_df['tydzien'] = passengers_df['data'].dt.isocalendar().week
print(passengers_df)

liczba_pasazerow = passengers_df['dzien_tygodnia'].groupby(passengers_df['tydzien'], group_keys=True).value_counts().sort_index().reset_index()

print(liczba_pasazerow)



model = LinearRegression()
inputs = liczba_pasazerow.index.values.reshape(-1,1)
targets = liczba_pasazerow['count']
model.fit(inputs, targets)


predictions = model.predict(inputs)
print(f' RMSE: {rmse(targets, predictions)}')



plt.plot(inputs, predictions, color='red')
plt.scatter(inputs, targets, s = 8, alpha=0.8)
plt.xlabel('Dzień')
plt.ylabel('liczba osób')
plt.legend(['Linia Regresji', 'Dane'])
plt.show()
