from flask import Flask, request
import pickle

app = Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/', methods = ['GET'])
def home(): 
    return "Welcome to the Loan Management System!!!"
     
@app.route('/predict', methods = ['GET'])
def predict(): 
    return "I predict your loan approval status."

@app.route('/make_predict', methods = ['GET', 'POST'])
def make_prediction():
    if request.method == 'GET':
        return "Please send a POST request with JSON data."
    data = request.get_json()
    # print(data)

    if data['Gender'] == "Male":
        gender = 0
    else:   
        gender = 1

    if data['Married'] == "Yes":
        married = 0
    else:
        married = 1
    
    input_features = [[gender, married, data["ApplicantIncome"], data['LoanAmount'], data['Credit_History']]]
    print(input_features)
    result = model.predict(input_features)
    if result[0] == 1:
        result = f"{{'prediction': 'Approved'}}"
    else:   
        result = f"{{'prediction': 'Rejected'}}"
    
    return {"Loan Approval Status": result}


if __name__ == '__main__':
    app.run(debug=True) 