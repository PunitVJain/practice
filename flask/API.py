
from flask import Flask, request


app = Flask(__name__)
@app.route('/api/login', methods=["GET", "POST"])
def login_page():
    _json = request.json
    username = _json["username"]
    password = _json["password"]
    return  {"password": password, "username": username}


if __name__ == "__main__":
    app.run(debug=True, port= 3300)

