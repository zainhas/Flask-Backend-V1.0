from flask import Flask, request, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy


#Flask Configuration
app = Flask(__name__, instance_relative_config=True)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Project S/StethoBackend/Flask-Backend-V1_0/flaskr/db.sqlite3' #Connect to sqlite database
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' #Connect to sqlite database
from flaskr.views import sound_api_Blueprint
app.register_blueprint(sound_api_Blueprint)


db.create_all()

if __name__ == '__main__':
	print "Starting Server"
	app.run(debug=True) #Remove Debug for production run