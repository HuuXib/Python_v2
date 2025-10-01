import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# EXERCISE: Are two separate linear regression models, one for smokers and one of non-smokers, better than a single linear regression model?
# Why or why not? Try it out and see if you can justify your answer with data.




medical_df = pd.read_csv('medical.csv')

smokers_df = medical_df[medical_df.smoker == 'yes']



#lets add sex_code

sex_codes = {'male':0, 'female':1}
smokers_df['sex_code'] = smokers_df.sex.map(sex_codes)


from sklearn import preprocessing

#Transforming region data into array to represent this data using one hot encoding method 
enc = preprocessing.OneHotEncoder()
enc.fit(smokers_df[['region']])
enc.categories_
one_hot = enc.transform(smokers_df[['region']]).toarray()

smokers_df.loc[:, ['northeast', 'northwest', 'southeast', 'southwest']] = one_hot



#create inputs and targets

inputs , targets = smokers_df[['age','bmi','children','sex_code', 'northeast', 'northwest', 'southeast', 'southwest']] , smokers_df.charges

model = LinearRegression()

model.fit(inputs,targets)
predictions = model.predict(inputs)

def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))
print(rmse(targets, predictions))

#Now lets see the actual weights of our features 
model.coef_

model.intercept_

