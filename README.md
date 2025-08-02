#  Loan Approval Prediction Web App

A Flask-based machine learning web application that predicts whether a loan will be approved based on user inputs like gender, marital status, income, loan amount, and credit history using Logistic Regression.

---

##  Features

- Logistic Regression-based ML Model
- Beautiful responsive UI with smooth gradients and shadows
- Accepts human-friendly inputs (e.g., Male/Female instead of 1/0)
- Instant prediction of loan approval
- Mobile-friendly and production-ready design

---

##  Project Structure
```
LoanApprovalPredictor/
│
├── static/
│ └── style.css # Custom CSS for UI
│
├── templates/
│ ├── index.html # Input form page
│ └── result.html # Prediction result page
│
├── model/
│ └── logistic_model.pkl # Trained Logistic Regression model
│
├── app.py # Main Flask app
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── sample_data.csv # Sample dataset for reference
```
---

##  Machine Learning Model

- **Algorithm:** Logistic Regression
- **Features Used:**
  - Gender (Male/Female)
  - Married (Yes/No)
  - Applicant Income
  - Loan Amount
  - Credit History (1/0)
- **Target:** Loan_Status (Approved/Rejected)

---

## Sample Input
```
Gender: Male
Married: Yes
Applicant Income: 5000
Loan Amount: 200
Credit History: 1
```
---

## Output
```
Loan Status: Approved 
```
---

##  Setup Instructions

Clone the repository

```
git clone https://github.com/your-username/LoanApprovalPredictor.git
cd LoanApprovalPredictor
```
Install dependencies
```
pip install -r requirements.txt
```
Run the Flask app
```
python app.py
```
Open in Browser
http://127.0.0.1:5000/

## Dataset Format (sample_data.csv)
Gender	Married	ApplicantIncome	LoanAmount	Credit_History	Loan_Status
Male	Yes	5000	200	1	1
Female	No	3000	120	0	0

## Screenshots
![alt text](<Screenshot 2025-08-02 143310.png>)
![alt text](<Screenshot 2025-08-02 143255.png>)
![alt text](<Screenshot 2025-08-02 143303.png>)

## Future Improvements
Add support for more features (education, dependents, property area)

Store input/output logs in a database

Deploy on platforms like Heroku or Render