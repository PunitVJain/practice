
from flask import Flask, request


app = Flask(__name__)
@app.route('/api/login', methods=["GET", "POST"])
def login_page():
    _json = request.json
    _username = _json["username"]
    _password = _json["password"]
    return  {"username": _username, "password": _password}


if __name__ == "__main__":
    app.run(debug=True)

