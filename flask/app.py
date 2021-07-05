# learning flask 

from flask import Flask, render_template, session, redirect, g, url_for
import os

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