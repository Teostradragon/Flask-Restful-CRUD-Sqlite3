from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

# auth， JWT Token
class UserTest:
    def __init__(self, _id, username, password, age):
        self.id = _id
        self.username = username
        self.password = password
        self.age = age

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,

                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('age',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
  # Read one user
    def get(self, username):
        user = self.find_by_username(username)
        if user:
            return user
        return {'message': 'User not found'}, 404

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'user':{'id': row[0],'username': row[1], 'password': row[2],'age': row[3]}}

# Create a new user
    def post(self,username):
        if self.find_by_username(username):
            return {'message': "username '{}' already exists.".format(username)}, 400

        data = User.parser.parse_args()

        user = {'username': username, 'password': data['password'], 'age': data['age']}

        try:
            User.insert(user)
        except:
            return {"message": "An error occurred inserting the user."}

        return user

    @classmethod
    def insert(cls, user):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?,?)"
        cursor.execute(query, (user['username'], user['password'], user['age']))

        connection.commit()
        connection.close()
        return {"message": "User created successfully."}, 201


# Delete one item
    def delete(self, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM users WHERE username=?"
        cursor.execute(query, (username,))

        connection.commit()
        connection.close()

        return {'message': 'user deleted'}

# Updates one user
    def put(self, username):
        data = User.parser.parse_args()
        user = self.find_by_username(username)
        updated_user = {'username': username, 'password': data['password'], 'age': data['age']}
        if user is None:
            try:
                User.insert(updated_user)
            except:
                return {"message": "An error occurred inserting the user."}
        else:
            try:
                User.update(updated_user)
            except:
                return {"message": "An error occurred updating the user."}
        return updated_user

    @classmethod
    def update(cls, user):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE users SET password=? age=? WHERE username=?"
        cursor.execute(query, (user['username'], user['password'], user['age']))

        connection.commit()
        connection.close()

  # Read all users, but should add token in header
class UserList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users"
        result = cursor.execute(query)
        users = []
        for row in result:
            users.append({'id': row[0],'username': row[1], 'password': row[2],'age': row[3]})
        connection.close()

        return {'Users': users}


