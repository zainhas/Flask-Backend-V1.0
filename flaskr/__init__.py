from flask import Flask, request, send_from_directory, abort
from flask_restful import Resource, Api, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


#Flask Configuration
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' #Connect to sqlite database
db = SQLAlchemy(app)



if __name__ == '__main__':
    app.run(debug=True) #Remove Debug for production run