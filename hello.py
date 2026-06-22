from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/ping')
def ping():
    return f"Hello, SARAVANAKUMAR KANNAN!"