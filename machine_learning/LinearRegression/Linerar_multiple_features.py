import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression



medical_df = pd.read_csv('medical.csv')


smokers_df = medical_df[medical_df.smoker == 'yes']


inputs = smokers_df[['age', 'bmi', 'children']]
targets = smokers_df.charges



model = LinearRegression()

model.fit(inputs, targets)
predictions = model.predict(inputs)

def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))


loss = rmse(targets, predictions)

print(f'Loss: {loss}')

#finding the correlations 

charges_bmi_correlation =  smokers_df.charges.corr(smokers_df.bmi)


fig = px.scatter(smokers_df, x='bmi', y='charges', title='BMI vs Charges')
fig.update_traces(marker_size=5)

fig.show()

#w
print(model.coef_)
    
#b

print(model.intercept_)


charges_children_correlation = smokers_df.charges.corr(smokers_df.children)

print(charges_children_correlation)

