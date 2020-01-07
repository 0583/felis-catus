#!/usr/bin/env python3

import json
import time

import psycopg2
import psycopg2.extensions

from flask import jsonify, redirect
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

from model import Entry
from config import app, db
from consts import DEBUG, PORT, DB_NAME, USER_NAME, PASSWORD, DOMAIN_NAME

migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Entry=Entry)


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', Server(host="0.0.0.0", port=PORT))
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
        try:
            conn = psycopg2.connect(database=DB_NAME,
                                    user=USER_NAME,
                                    password=PASSWORD,
                                    host=DOMAIN_NAME)
        except:
            return jsonify(error_response())
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

    if response and len(response) == 3:
        return redirect(response[2], code=302)
    else:
        return jsonify(error_response())


if __name__ == "__main__":
    manager.run()
