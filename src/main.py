#!/usr/bin/env python3

import json
import time

import psycopg2
import psycopg2.extensions

from flask import jsonify, redirect
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from model import Entry
from config import app, db
from consts import DEBUG, PORT

migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Entry=Entry)


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

conn = None


def error_response():
    return {
        'status': 'error',
        'info': 'invalid_short_link',
        'timestamp': int(time.time())
    }


@app.route('/t/<short_link>', methods=['GET'])
def Redirect(short_link):
    global conn
    if not conn:
        conn = psycopg2.connect(
            database='felisdb', user='felis', password='', host='localhost')
    sql = 'SELECT * FROM "pairs" WHERE short_link = \'{0}\''.format(
        str(short_link))

    print(sql)
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except:
        return jsonify(error_response())
    response = cur.fetchone()
    cur.close()

    if len(response) == 3:
        return redirect(response[2], code=302)
    else:
        return jsonify(error_response())


if __name__ == "__main__":
    manager.run()