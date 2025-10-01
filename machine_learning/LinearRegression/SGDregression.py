
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 
from sklearn.linear_model import SGDRegressor

medical_df = pd.read_csv('medical.csv')
smokers_df = medical_df[medical_df.smoker == 'yes']
def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))


inputs = smokers_df[['age']]
targets = smokers_df.charges

from sklearn.preprocessing import StandardScaler


#This two lines of code make SGD regression works properly 


#makes an scaler object that normalizes our data 
scaler = StandardScaler()
#this line fits the scaler into our inputs
inputs = scaler.fit_transform(inputs)




model = SGDRegressor()
model.fit(inputs, targets)



def plotdata(inputs, targets):
    model.fit(inputs, targets)
    predictions = model.predict(inputs)

    #print significant data
    print(inputs)
    print(predictions)
    print (rmse(targets, predictions))

    plt.plot(inputs, predictions, 'r-',alpha =0.9)

    plt.scatter(inputs, targets, s = 8, alpha = 0.8)

    plt.xlabel('Age')
    plt.ylabel('charges')

    plt.legend(['Predicted', 'Actual'])
    plt.show()

plotdata(inputs, targets)