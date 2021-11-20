
from flask import Flask, json, request, jsonify
from flask_restful import Api, Resource




app = Flask(__name__)
api = Api(app)

@app.route('/api/login', methods=["GET", "POST"])
def login_page():
    _json = request.json
    _username = _json["username"]
    _password = _json["password"]
    return  {"password": _password, "username": _username}

data = {"name":["Punit Jain", "Vinod Jain", "Ram Jain"]}

class Sample(Resource):

    def get(self):
        return "Hello World!"

class SecondApi(Resource):

    def post(self):
        name = request.get_json()
        print(name)
        if name["name"] in data["name"]:
            return jsonify({"data is there ":name})
        return jsonify({"data is not there ":name})

api.add_resource(Sample, "/api/helloworld")
api.add_resource(SecondApi, "/api/test")


if __name__ == "__main__":
    app.run(debug=True, port= 3300)

