from flask import request, redirect, url_for, abort, jsonify,send_from_directory, Blueprint, make_response
from flask_restful import Resource, marshal_with, fields
from flaskr.models import SoundData
import datetime
from flaskr import db
from flask_restful import Api

sound_api_Blueprint = Blueprint('sound_api', __name__)


#Error Handling
api = Api(sound_api_Blueprint)

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
		pass

class sound_metadata(Resource):
	@marshal_with(sound_resource, envelope=sound_resource)
	def get(self, id): #get single metadata, then return marshalled object
		return SoundData.query.get_or_404(id)

	def post(self):
		new_sound_data = SoundData()
		new_sound_data.import_metadata(request) #Pass flask request object to model
		db.session.add(new_sound_data)
		db.session.commit()
		return jsonify({}), 201, {'Data': str(new_sound_data.get_date())}

class serve_file(Resource):
	def get(self, path):
		return send_from_directory('../uploads', path)

class delete_sound_file(Resource):
	def get(self, id):
		pass

class delete_sound_files(Resource):
	def get(self):
		pass

#class test_api(Resource):
#	@marshal_with(sound_resource, envelope=sound_resource)

@sound_api_Blueprint.route('/test',methods = ['GET'])
def test():
	# Pass flask request object to model
	new_sound_data = SoundData(name="Test1", file_uri="SoundPratik", length=1234, date=datetime.datetime.now())
	print 'Created Example'
	db.session.add(new_sound_data)
	db.session.commit()
	return jsonify(new_sound_data.export_data())

class sound_file(Resource):
	def get(self,id):
		sound_file = SoundData.query.get_or_404(id)
		return redirect(url_for('serve_file', path=sound_file.file_uri))

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
api.add_resource(serve_file, '/api/v1_0/file/<string:path>')
api.add_resource(delete_sound_file, '/api/v1_0/delete/<int:id>')
api.add_resource(delete_sound_files, '/api/v1_0/deleteall')
api.add_resource(analyze_sound_file, '/api/v1_0/analyze/<int:id>')
#api.add_resource(test_api,'/test')