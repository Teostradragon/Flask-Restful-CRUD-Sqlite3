# Flask RESTful API SQLite3

created with Python `flask` , `flask_restful` and `flask_jwt`.

`authentication` has been applied with `flask_jwt`.

## How to run the project

python create_table.py

python app.py

The API information will be stored in a file `data.db` which will act as the SQLite database.
To generate this file, _and with it the tables_, run `create_table.py` before running `app.py`.

You will then be able to Create new users, Authenticate and CRUD item(s).



##
create a new user: localhost:5000/User/<string:username>

Authenticates existing user: localhost:5000/auth

Reads one user: http://127.0.0.1:5000/User/<string:username>

Reads all users: localhost:5000/users

Updates one user: localhost:5000/User/<string:username>

Deletes one user: localhost:5000/User/<string:username>

- POST `localhost:5000/auth` : Authenticates existing user. Provides an `access token`.
  This token must be included on the headers of all the following requests. `Authorization = JWT <token>`
