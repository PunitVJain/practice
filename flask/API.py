
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

data = {"name":"Punit Jain"}

class Sample(Resource):

    def get(self):
        return "Hello World!"

class SecondApi(Resource):

    def post(self, data):
        name = request.json["name"]
        if name in data.keys():
            return({"My Name is": name})
        return({"My Name is not in data"})

api.add_resource(Sample, "/api/helloworld")
api.add_resource(SecondApi, "/api/test")


if __name__ == "__main__":
    app.run(debug=True, port= 3300)

