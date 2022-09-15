from werkzeug.security import safe_str_cmp
from user import UserTest


def authenticate(username, password):
    user = UserTest.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserTest.find_by_id(user_id)

