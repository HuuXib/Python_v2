import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

medical_df = pd.read_csv('medical.csv')

smokers_df = medical_df[medical_df.smoker == 'yes']


#functions

def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))

def plot_regression_line(bmi, charges, predictions):
    plt.plot(bmi,predictions, 'r-', alpha=0.9)
    plt.scatter(bmi, charges,s=8, alpha=0.8)
    plt.grid()
    plt.xlabel('BMI')
    plt.ylabel('Charges')
    plt.legend(['Estimate', 'Actual'])
    plt.show()

def show_model_info(targets, predictions):
    print(f"RMSE: {rmse(targets, predictions)}")
    print(f"Correlation coeficient: {smokers_df.bmi.corr(smokers_df.charges)}")
    print(f"w coefficient: {model.coef_} \nBias: {model.intercept_}")


inputs = smokers_df[['bmi']]
targets = smokers_df.charges

model = LinearRegression()
model.fit(inputs, targets)

predictions = model.predict(inputs)

show_model_info(targets, predictions)
plot_regression_line(inputs,targets,predictions)