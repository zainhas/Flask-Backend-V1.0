from flask import request, app, flash, redirect, url_for, render_template, abort, json
from flask_sqlalchemy import SQLAlchemy
from flaskr import db


class SoundData(db.Model,object):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, unique=False, nullable=False)
    file_uri = db.Column(db.String, unique=False, nullable=True)
    length = db.Column(db.Integer, unique=False, nullable=True)
    data = db.Column(db.Date, unique=False, nullable=True)

    def __init__(self, user = None, filename = None, length=None, date=None):
        self.user = user
        self.file_uri = filename
        self.length = length
        self.date = date

    def __repr__(self):
        return '<id: {}, user: {}, filename: {}>'.format(self.id, self.user, self.filename)

    def export_data(self):
        return {
            'id': self.id,
            'user': self.user,
            'file_uri': self.file_uri
        }
    #Called from Views
    def import_metadata(self, request):
        try:
            json_data = request.get_json()
            if 'user' in json_data:
                self.user = json_data['user']
            if 'filename' in json_data:
                self.filename = json_data['filename']
            if 'length' in json_data:
                self.length = json_data['length']
            if 'date' in json_data:
                self.date = json_data['date']
        except KeyError as e:
            print "Key not found in metadata"
        return self

    def import_data(self, request):
        pass

