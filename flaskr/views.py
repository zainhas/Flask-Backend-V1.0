from flaskr import db, api, app
from flask_restful import Resource, marshal_with, fields
from flaskr.models import SoundData
from flask import Blueprint, request, redirect, url_for, abort, jsonify


#Sound MetaDeta Return
sound_resource = {
	'id' : fields.Integer,
	'user': fields.String,
	'file_uri':fields.String,
	'length': fields.Integer,
	'date': fields.DateTime
}

class sound_get_all(Resource):
	def get(self): #Get all sound data files in server
		pass

class sound_metadata(Resource):
	@marshal_with(sound_resource, envelope=sound_resource)
	def get(self, id): #get single metadata, then return marshalled object
		return SoundData.query.get_or_404(id)

	@marshal_with(sound_resource, envelope=sound_resource)
	def post(self):
		new_sound_data = SoundData()
		new_sound_data.import_metadata(request) #Pass flask request object to model
		db.session.add(new_sound_data)
		db.session.commit()
		return jsonify({}), 201, {'Location': new_sound_data.get_url()}

class sound_file(Resource):
	def get(self,id):
		pass

	def post(self,id):
		data = SoundData.query.get_or_404(id)
		if data:
			content = request.data #Incoming Data as String


#Flask-Restful Api add URL Redirect
api.add_resource(sound_get_all, '/api/v1_0/soundmetadatas')
api.add_resource(sound_metadata, '/api/v1_0/soundmetadata/<int:id>')
api.add_resource(sound_file, '/api/v1_0/sounddata/<int:id>')
