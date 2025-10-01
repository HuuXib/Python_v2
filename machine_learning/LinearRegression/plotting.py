import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


medical_df = pd.read_csv('medical.csv')
medical_df
medical_df.info() # give us information about column types etc.
medical_df.describe() # give us some information about data in our csv


#The following settings will improve the default style and font sizes for our charts.
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10,6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

medical_df.age.describe()

fig = px.histogram(medical_df, 
                   x = 'bmi',
                   marginal= 'box',
                   color_discrete_sequence=['red'],
                   nbins=47,
                   title='Distributrion of BMI')
# fig.update_layout(bargap=0.1)
# fig.show()

fig_smoker = px.histogram(medical_df, 
                   x = 'charges',
                   marginal= 'box',
                   color = 'smoker',
                   color_discrete_sequence=['green','grey'],
                   title='Anual Medical Charges')
# fig_smoker.update_layout(bargap=0.1)
# fig_smoker.show()

medical_df.smoker.value_counts()

fig_sexsmoker = px.histogram(medical_df, x = 'smoker', color='sex', title='Smoker')


fig_ageandcharges = px.scatter(medical_df,x = 'age', y = 'charges', color ='smoker',opacity=0.8,hover_data=['sex'], title='charges depended on age')
fig_ageandcharges.update_traces(marker_size = 5)
# fig_ageandcharges.show()


fig_BMIandcharges = px.scatter(medical_df,x = 'bmi', y = 'charges', color ='smoker',opacity=0.8,hover_data=['sex'], title='BMI vs Charges')
# fig_ageandcharges.update_traces(marker_size = 5)
# fig_BMIandcharges.show()



# EXERCISE: Create some more graphs to visualize how the "charges" column is related to other columns ("children", "sex", "region" and "smoker"). Summarize the insights gathered from these graphs.

fig_charchil = px.violin(medical_df, x = 'region', y = 'charges' , color='smoker',hover_data=['sex'], title = 'region vs charges',)

print (medical_df.charges.corr(medical_df.age))
# fig_charchil.show()

#if data is a boolean value we can convert it into 0 or 1 like this 
smoker_values = {'no': 0, 'yes': 1}
smoker_numeric = medical_df.smoker.map(smoker_values)
print(medical_df.charges.corr(smoker_numeric))


#this line select all integer datatypes because i wanted to make heatmap and i had error because pd was selecting chars strings etc.
numeric_df = medical_df.select_dtypes(include=['number'])
print(numeric_df.corr())


sns.heatmap(numeric_df.corr(), cmap='Reds', annot=True)
plt.title('Correlation Matrix')
plt.show()

