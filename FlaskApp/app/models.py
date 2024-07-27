from flask_bcrypt import Bcrypt
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
        return list(mongo.db.Users.find())

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
