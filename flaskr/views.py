from flaskr import db, api, app
from flask_restful import Resource, marshal_with, fields
from flaskr.models import SoundData
from flask import Blueprint, request, redirect, url_for, abort, jsonify

class create_test_metadata(Resource):
	def post(self):
		new_data = SoundData()
		new_data.import_metadata(request) #Pass flask request object to model
		db.session.add(new_data)
		db.session.commit()



#Flask-Restful Api add URL Redirect
api.add_resource(create_test_metadata, '/upload/<string:id>')