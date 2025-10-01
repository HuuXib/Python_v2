import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

medical_df = pd.read_csv('medical.csv')

numeric_cols = ['age', 'bmi', 'children']
scaler = StandardScaler()
scaler.fit(medical_df[numeric_cols])
scaler.mean_ #computes actual mean of our scaled dataframes
scaler.var_ #computes variation of our data (variation measuers how enormous is our data range)


#we can now scale our data as follows (as follows = w następujący sposób)
scaled_inputs = scaler.transform(medical_df[numeric_cols])


smoker_codes = {'no':0, 'yes':1}

#this line makes another column called smoker_code which represents smoker column with number code (yes = 1:no = 0)
medical_df['smoker_code'] = medical_df.smoker.map(smoker_codes)
print(medical_df)

#now lets calculate correlation strenght between charges and smoker_code
print(medical_df.charges.corr(medical_df.smoker_code))

#lets add sex_code
sex_codes = {'male':0, 'female':1}
medical_df['sex_code'] = medical_df.sex.map(sex_codes)

#Transforming region data into array to represent this data using one hot encoding method 
enc = preprocessing.OneHotEncoder()
enc.fit(medical_df[['region']])
enc.categories_
one_hot = enc.transform(medical_df[['region']]).toarray()

medical_df[['northeast', 'northwest', 'southeast', 'southwest']] = one_hot

#now lets 'import' categorical data
cat_cols = ['smoker_code', 'sex_code', 'northeast', 'northwest', 'southeast', 'southwest']
categorical_data = medical_df[cat_cols].values

#np.concatenate - combines two tables into one array

#our ml data
inputs = np.concatenate((scaled_inputs, categorical_data), axis = 1) #axis is integer value that tells our data to be connected horizontally(0) or verthically(1)
targets = medical_df.charges


#Create and train the model
model = LinearRegression()
model.fit(inputs,targets)

#generate predictions
predictions = model.predict(inputs)

#lets again make an rmse function
def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))

#calculate the loss(rmse)
loss = rmse(targets, predictions)
print(f'Loss: {loss}')

#we can now compare weights and its features into one Dataframe
weights_df = pd.DataFrame({
    'feature': np.append(numeric_cols + cat_cols, 1),
    'weight': np.append(model.coef_, model.intercept_)
})
weights_df.sort_values('weight', ascending=False) # Ascending - Rosnąco
print(weights_df)

#Creating a Test Set

from sklearn.model_selection import train_test_split