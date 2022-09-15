# Flask RESTful API SQLite3

created with Python `flask` , `flask_restful` and `flask_jwt`.

`authentication` has been applied with `flask_jwt`.

## How tp run the project

The API information will be stored in a file `data.db` which will act as the SQLite database.
To generate this file, _and with it the tables_, run `create_table.py` before running `app.py`.

You will then be able to Create new users, Authenticate and CRUD item(s).

##

- POST `localhost:5000/auth` : Authenticates existing user. Provides an `access token`.
  This token must be included on the headers of all the following requests. `Authorization = JWT <token>`
