#Importing the Dependencies
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
#Data Collection and Analysis

#PIMA Diabetes Dataset
# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('diabetes.csv') 
# printing the first 5 rows of the dataset
diabetes_dataset.head()
# number of rows and Columns in this dataset
diabetes_dataset.shape
# getting the statistical measures of the data
diabetes_dataset.describe()
diabetes_dataset['Outcome'].value_counts()
diabetes_dataset.groupby('Outcome').mean()
# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']
print(X)
print(Y)
#Data Visuaization
import matplotlib as plt
diabetes_dataset.hist(figsize=(20,20))
#Correlation of dataset
diabetes_dataset.corr()
#SNS pair plot
import seaborn as sns
sns.pairplot(diabetes_dataset,diag_kind='kde');
df_t = diabetes_dataset
df_t['Outcome'].astype('category')
df_t['Outcome'].replace(0,"non-diabetic",inplace=True)
df_t['Outcome'].replace(1,"diabetic",inplace=True)

sns.pairplot(df_t,hue='Outcome',diag_kind='kde');
#Train Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
#Training the Model
classifier = svm.SVC(kernel='linear')
#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)
#SVC(kernel='linear')
#Model Evaluation
#Accuracy Score
# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data : ', training_data_accuracy)
# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data : ', test_data_accuracy)
#Making a Predictive System
input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')   
#Saving the trained model
import pickle
filename = 'trained_model.pkl'
pickle.dump(classifier, open(filename, 'wb'))
# loading the saved model
loaded_model = pickle.load(open('trained_model.pkl', 'rb'))    
input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')
