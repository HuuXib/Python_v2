import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

medical_df = pd.read_csv('medical.csv')

sns.barplot(data=medical_df, x='smoker', y = 'charges')
plt.show()

#we can use number code for our smoker column 
smoker_codes = {'no':0, 'yes':1}

#this line makes another column called smoker_code which represents smoker column with number code (yes = 1:no = 0)
medical_df['smoker_code'] = medical_df.smoker.map(smoker_codes)
print(medical_df)

#now lets calculate correlation strenght between charges and smoker_code
print(medical_df.charges.corr(medical_df.smoker_code))

#lets add sex_code

sex_codes = {'male':0, 'female':1}
medical_df['sex_code'] = medical_df.sex.map(sex_codes)


from sklearn import preprocessing

#Transforming region data into array to represent this data using one hot encoding method 
enc = preprocessing.OneHotEncoder()
enc.fit(medical_df[['region']])
enc.categories_
one_hot = enc.transform(medical_df[['region']]).toarray()

medical_df[['northeast', 'northwest', 'southeast', 'southwest']] = one_hot


#create inputs and targets

inputs , targets = medical_df[['age','bmi','children', 'smoker_code','sex_code', 'northeast', 'northwest', 'southeast', 'southwest']] , medical_df.charges

model = LinearRegression()

model.fit(inputs,targets)
predictions = model.predict(inputs)

def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))
print(rmse(targets, predictions))