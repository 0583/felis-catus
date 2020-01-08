#!/usr/bin/env python

from consts import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

LOCAL_RUN = False
if LOCAL_RUN:
    HOST = 'localhost'
else:
    HOST = 'felisdb'

app.config['DEBUG'] = DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s/%s' % (
    USER_NAME, PASSWORD, HOST, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)
