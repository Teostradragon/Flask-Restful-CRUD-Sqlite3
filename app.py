from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import  User,UserList, UserTest

app = Flask(__name__)
app.secret_key = 'nery'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserList, '/users')
api.add_resource(User, '/User/<string:username>')

# avoids running app from an import
# will run only if the file is being executed from running app.py
if __name__ == '__main__':
    app.run(port=5000, debug=True)

