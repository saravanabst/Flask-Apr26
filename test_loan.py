import pytest
from loan import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.text == "Welcome to the Loan Management System!!!"


def test_predict_million(client):

    data = {
        "Gender": "Male",
        "Married": "Yes",
        "ApplicantIncome": 5000,
        "LoanAmount": 1000000,
        "Credit_History": 1
    }

    response = client.post('/make_predict', json=data)
    assert response.status_code == 200
    assert response.json == {"Loan Approval Status": "{'prediction': 'Rejected'}"}

def test_predict_low_amt(client):
    data = {
        "Gender": "Male",
        "Married": "Yes",
        "ApplicantIncome": 5000,
        "LoanAmount": 100,
        "Credit_History": 1
    }

    response = client.post('/make_predict', json=data)
    assert response.status_code == 200
    assert response.json == {"Loan Approval Status": "{'prediction': 'Approved'}"}

#def test_loan_calculation(client):
    #response = client.post('http://localhost:5000/make_predict', json={})
    