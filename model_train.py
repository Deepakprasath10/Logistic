import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv('loan_data.csv')

df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

X = df[['Gender', 'Married', 'ApplicantIncome', 'LoanAmount', 'Credit_History']]
y = df['Loan_Status']

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open('logistic_model.pkl', 'wb'))
