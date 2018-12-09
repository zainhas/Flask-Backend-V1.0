from flask import Flask, request, send_from_directory, abort, Blueprint
from flask_sqlalchemy import SQLAlchemy

#Flask Configuration
app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' #Connect to sqlite database
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
from flaskr.views import sound_api_Blueprint
app.register_blueprint(sound_api_Blueprint)


if __name__ == '__main__':
	app.run(debug=True) #Remove Debug for production run