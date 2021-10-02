from flask import Flask

app = Flask(__name__)
@app.route('/', method=["GET", "POST"])
def login_page():
    pass
