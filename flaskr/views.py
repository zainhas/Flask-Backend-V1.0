#Create Blueprint
from flask import request, redirect, url_for, abort, jsonify,send_from_directory, Blueprint
from flask_restful import Resource, fields, Api
from flaskr.models import SoundData
from flaskr import db
import datetime
import os

sound_api_Blueprint = Blueprint('sound_api', __name__)
api = Api(sound_api_Blueprint) #Create Flask Api
db.create_all()

#Sound MetaDeta Return
sound_resource = {
	'id' : fields.Integer,
	'name': fields.String,
	'file_uri':fields.String,
	'length': fields.Integer,
	'date': fields.DateTime
}

class sound_get_all(Resource):
	def get(self): #Get all sound data files in server
		return jsonify({'Sound Datas': [SoundData.query.get_or_404(Sound.id).export_data() \
		for Sound in SoundData.query.all()]})

class sound_metadata(Resource):
	def get(self, id): #get single metadata, then return marshalled object
		return jsonify(SoundData.query.get_or_404(id).export_data())

	def post(self):
		new_sound_data = SoundData()
		new_sound_data.import_metadata(request) #Pass flask request object to model
		db.session.add(new_sound_data)
		db.session.commit()
		return jsonify({}), 201, {'Date': str(new_sound_data.get_date())}

class serve_file(Resource):
	def get(self, filename):
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
		return send_from_directory(path, filename)

class delete_sound_file(Resource):
	def get(self, id):
		sounddata = SoundData.query.get_or_404(id)
		#Delete File
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
		if(os.path.exists(os.path.join(path, sounddata.file_uri))):
			os.remove(os.path.join(path, sounddata.file_uri))
		#Remove From database
		db.session.delete(sounddata)
		db.session.commit()


class delete_sound_files(Resource):
	def get(self):
		db.drop_all()
		db.create_all()

class test_api(Resource):
	def get(self):
		new_sound_data = SoundData(name="Test1", file_uri="SoundPratik.dat", length=1234, date=datetime.datetime.now())
		db.session.add(new_sound_data)
		db.session.commit()
		return jsonify(new_sound_data.export_data())

class sound_file(Resource):
	def get(self,id):
		sound_file = SoundData.query.get_or_404(id)
		return redirect(url_for('serve_file', filename=sound_file.file_uri, _method = "GET"))

	def post(self,id):
		sound_file = SoundData.query.get_or_404(id)
		if sound_file:
			sounddata = request.data #Incoming Data as String
			fn = 'StethoData_%s_%s.dat' %(request.date, id)
			with open(fn, 'wb') as fp:
				fp.write(sounddata) #Write the sound data
			sound_file.file_uri = fn
			db.session.add(sound_file) #Update the SQL Data field for file URI
			db.session.commit()
			return ('', 204) #Return No Content To Return
		abort(404)

#Analysis API's
class analyze_sound_file(Resource):
	def get(self, id):
		#get sound file uri
		#send data to ml function
		#when processing is finished return
		pass

#Flask-Restful Api add URL Redirect
api.add_resource(sound_get_all, '/api/v1_0/soundmetadatas')
api.add_resource(sound_metadata, '/api/v1_0/soundmetadata/<int:id>')
api.add_resource(sound_file, '/api/v1_0/sounddata/<int:id>')
api.add_resource(serve_file, '/api/v1_0/file/<string:filename>')
api.add_resource(delete_sound_file, '/api/v1_0/delete/<int:id>')
api.add_resource(delete_sound_files, '/api/v1_0/deleteall')
api.add_resource(analyze_sound_file, '/api/v1_0/analyze/<int:id>')
api.add_resource(test_api,'/api/v1_0/test')