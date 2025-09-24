import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression

medical_df = pd.read_csv('medical.csv')

# Now im gonna separate smoker people 

smokers_df = medical_df[medical_df.smoker == 'yes']


#RMSE function to calculate how actually bad or good our model is 
def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))



# Select only numeric data 

numeric_df = smokers_df.select_dtypes(include='number')

#lets make correlation heatmap 
#numeric_df.corr counts actual colleration matrix between numeric columns
#annot (adnotation) variable just shows the actual value inside every "box" 
sns.heatmap(numeric_df.corr(), cmap='Reds', annot=True)
plt.title("Correlation heatmap")
plt.show()


#now lets train our model and make some predictions

model = LinearRegression()

#now lets make our inputs and predictions variables
inputs = smokers_df[['age']]
targets = smokers_df.charges

#first we have to fit inputs and targets and only then we can predict anything !
# predictions = model.predict(inputs)






#the RMSE seems to be above our tolerance limit 

#lets try to plot our regression line 


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