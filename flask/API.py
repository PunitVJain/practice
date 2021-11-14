
from flask import Flask, request
from flask_restful import Api, Resource



app = Flask(__name__)
api = Api(app)

@app.route('/api/login', methods=["GET", "POST"])
def login_page():
    _json = request.json
    _username = _json["username"]
    _password = _json["password"]
    return  {"password": _password, "username": _username}


class Sample(Resource):

    def get(self):
        return "Hello World!"

api.add_resource(Sample, "/api/helloworld")


if __name__ == "__main__":
    app.run(debug=True, port= 3300)

