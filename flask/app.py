# learning flask 
# flask login API.

from flask import Flask, render_template, request
import os
from flask_restful import Api


app  =  Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_creds')
def login_creds():
    pass



if __name__ == '__main__':
    app.run(debug=True)