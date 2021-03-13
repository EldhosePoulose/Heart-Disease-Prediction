# Data Preprocessing

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('./metadata-Heart-Disease.csv')
print(df.head())
print(df.dtypes)
# print(df.isnull().sum())
df['Sex'] = df.Sex.astype('category') #Male=1; Female=0
df['CP'] = df.CP.astype('category') # chest pain type (1= typical angina; 2= atypical angina; 3= non-anginal pain; 4= asymptomatic)
# restecg presence of 0,1,2 why in Cleveland
df['exang'] = df.exang.astype('category') #exercise induced angina (1= Yes; 0= No)
df['slope'] = df.slope.astype('category') #the slope of the peak exercise ST segment (1= upsloping; 2= flat; 3= downsloping)
# df['ca'] = df.ca.astype('int64')
df['thal'] = df.thal.astype('category') #3= normal; 6= fixed defect; 7= reversable defect
df['Country'] = df.Country.astype('category') # Cleveland Hungarian Switzerland LongBeachVA
df['target'] = df.target.astype('category') # 0 or 1; diagnosis of heart disease (angiographic disease status, 0= <50% diameter narrowing; 1= >50% diameter narrowing)(the predicted attribute)
print(df.dtypes)


#
df2 = df.copy()
def chng(Sex):
    if Sex == 0:
        return 'female'
    else:
        return 'male'
df2['Sex'] = df2['Sex'].apply(chng)
def chng2(prob):
    if prob == 0:
        return 'Heart Disease'
    else:
        return 'No Heart Disease'
df2['target'] = df2['target'].apply(chng2)

df2['target'] = df2['target'].apply(chng2)
sns.countplot(data= df2, x='Sex',hue='target')
plt.title('Gender v/s target\n')
plt.show()

sns.countplot(data= df2, x='CP',hue='target')
plt.title('Chest Pain Type v/s target\n')
plt.show()

# Check why No Heart disease not on the plot