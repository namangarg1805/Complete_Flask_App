from flask import Flask,request
import pickle

app = Flask(__name__)

@app.route(rule="/",methods=["GET"])
def homepage():
    return "<h1>Welcome to our app</h1>"

pickle_file = open("classifier.pkl","rb")
model = pickle.load(pickle_file)

@app.route(rule="/prediction",methods=["POST"])
def prediction():
    loan_req = request.get_json()
    print(loan_req)
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    result = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}



