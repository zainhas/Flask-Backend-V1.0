from flask import Flask, request, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

#Flask Configuration
app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' #Connect to sqlite database
db = SQLAlchemy(app)

from flaskr.views import sound_api_Blueprint
app.register_blueprint(sound_api_Blueprint)


if __name__ == '__main__':
	db.create_all()
	app.run(debug=True) #Remove Debug for production run