from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()


class ConfigMongoDB:
    MONGO_URI = os.getenv('MONGO_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')


mongo = PyMongo()

class User:
    def createUser(data):
        user = {
            "firstName": data["firstName"],
            "lastName": data["lastName"],
            "email": data["email"],
            "password": data["password"]
        }

        return mongo.db.Users.insert_one(user)

    def fetchAllUsers():
        users = mongo.db.Users.find()
        fetchedUsers = []
        for user in users:
            data = {
                "_id": str(user["_id"]),
                "firstName": user["firstName"],
                "lastName": user["lastName"],
                "email": user["email"]}
            fetchedUsers.append(data)
            

        return fetchedUsers

    def fetchUserByEmail(email):
         return mongo.db.find_one({"email":email})

    def updateUser(email,data):
        updatedData = {}
        if "firstName" in data:
            updatedData["firstName"] = data["firstName"]
        if "lastName" in data:
            updatedData["lastName"] = data["lastName"]
        if "password" in data:
            updatedData["password"] = data["password"]

        return mongo.db.Users.update_one({"email":email},{"$set":updatedData})

    def deleteUser(email):
        return mongo.db.Users.delete_one({"email":email})


app = Flask(__name__)
app.config.from_object(ConfigMongoDB)
mongo.init_app(app)


@app.route('/')
def home():
    return "Welcome to CoRiderAssignment"


@app.route('/createUser',methods=['POST'])
def createUser():
    data = request.get_json()
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    email = data.get('email')
    password = data.get('password')

    if not firstName and not lastName and not email and not password:
        return jsonify({"message": "All fields are required"}), 400

    user = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": password
    }
    User.createUser(user)
    return jsonify({"message": "User created successfully"}), 201


@app.route("/fetchUsers",methods=['POST'])
def fetchUsers():
    users = User.fetchAllUsers()
    return jsonify(users)

@app.route('/update/<email>',methods=['POST'])
def updateUser(email):
    data = request.get_json()
    # email = data.get('email')
    User.updateUser(email,data)
    return jsonify({"message": "User updated successfully"}), 200


@app.route('/delete/<email>', methods=['DELETE'])
def deleteUser(email):
    User.deleteUser(email)
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
