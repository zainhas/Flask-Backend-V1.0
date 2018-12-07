from flaskr import db, api, app
from flask_restful import Resource, marshal_with, fields
from flaskr.models import SoundData
from flask import Blueprint, request, redirect, url_for, abort, jsonify

class sound_get_all(Resource):
	def get(self): #Get all sound data files in server
		pass

class sound_metadata(Resource):
	def get(self): #get single metadata
		pass

	def post(self):
		new_sound_data = SoundData()
		new_sound_data.import_metadata(request) #Pass flask request object to model
		db.session.add(new_sound_data)
		db.session.commit()
		return jsonify({}), 201, {'Location': new_sound_data.get_url()}



#Flask-Restful Api add URL Redirect
api.add_resource(sound_get_all, '/api/v1_0/sounddatas')
api.add_resource(sound_metadata, '/api/v1_0/soundata/<int:id>')
