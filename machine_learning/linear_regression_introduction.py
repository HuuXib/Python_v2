import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


medical_df = pd.read_csv('medical.csv')
medical_df

non_smoker_df = medical_df[medical_df.smoker == 'no']

# plt.title('Age vs Charges')
# sns.scatterplot(data=non_smoker_df , x = 'age', y = 'charges', alpha = 0.7, s=15)
# plt.show()


def estimate_charges(age, w, b):
    return w * age + b

w = 50
b = 100



#Lets define a function to calculate RMSE(root mean square error)


import numpy as np 
def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))

def try_parameters(w, b):
    ages = non_smoker_df.age
    predictions = estimate_charges(ages, w, b)
    target = non_smoker_df.charges
    plt.plot(ages, predictions, 'r-', alpha = 0.9)
    plt.scatter(ages, target , s=8,alpha=0.8)
    plt.xlabel("Age")
    plt.ylabel("estimated charges")
    plt.legend(['Estimate', 'Actual'])
    loss = rmse(target, predictions)
    print(f"RMSE loss: {loss}")
    plt.show()



#My best fit
# try_parameters(240,-1100)



targets = non_smoker_df['charges']
predicted = estimate_charges(non_smoker_df.age, w , b)

# print(rmse(targets, predicted))

#Now we will try to compute estimated line using linear regression 

from sklearn.linear_model import LinearRegression

model = LinearRegression()

#our input has to be a 2D tensor with more than one dimension

inputs = non_smoker_df[['age']]
targets = non_smoker_df.charges

print('inputs.shape :', inputs.shape)
print('targes.shape :', targets.shape)

model.fit(inputs, targets)
# print(
# model.predict(np.array([[23], 
#                         [37], 
#                         [61]])))

predictions = model.predict(inputs)
print(inputs)
print(predictions)
print(rmse(targets,predictions))

#its w value based on the alghoritm
print(model.coef_)

#its b value based on the alghoritm
print(model.intercept_)

#ok lets print given regression line 

plt.plot(inputs , predictions, 'r-', alpha = 0.9)
plt.scatter(inputs, targets, s=8, alpha=0.8)
plt.xlabel('Age')
plt.ylabel('Model prediction')
plt.legend(['Predicted', 'Actual'])
plt.show()