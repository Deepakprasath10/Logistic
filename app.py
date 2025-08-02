from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('logistic_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Convert form input values
    gender = request.form['gender'].strip().lower()
    married = request.form['married'].strip().lower()
    income = float(request.form['income'])
    loan = float(request.form['loan'])
    history = request.form['history'].strip()

    # Map values to numeric
    gender = 1 if gender == 'male' else 0
    married = 1 if married == 'yes' else 0
    history = 1 if history == 'yes' else 0

    data = [gender, married, income, loan, history]

    # Predict
    prediction = model.predict([data])[0]
    result = "✅ Approved" if prediction == 1 else "❌ Rejected"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
