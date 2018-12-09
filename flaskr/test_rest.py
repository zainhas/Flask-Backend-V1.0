
import unittest
from flaskr import app, db
from flask_restful import Resource
from flaskr.models import SoundData
from flask import jsonify
import datetime

#Testing within unittest module
class test_api(Resource):
	count = 0
	def get(self):
		new_sound_data = SoundData(name="Test1", file_uri="SoundPratik_%s.dat"%(test_api.count), length=1234, date=datetime.datetime.now())
		db.session.add(new_sound_data)
		db.session.commit()
		test_api.count +=1
		return jsonify(new_sound_data.export_data())


