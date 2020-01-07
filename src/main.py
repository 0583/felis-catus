#!/usr/bin/env python3

import json
import time
import random

import psycopg2
import psycopg2.extensions

from zlib import crc32
from flask import jsonify, redirect, render_template
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


def get_line_count():
    global conn
    if conn:
        try:
            sql = 'SELECT COUNT(*) FROM "pairs"'
            cur = conn.cursor()
            cur.execute(sql)
            response = cur.fetchone()
            print("obtained database line count: ", response)
            return response[0]
        except:
            return 0
    else:
        try:
            conn = psycopg2.connect(database=DB_NAME,
                                    user=USER_NAME,
                                    password=PASSWORD,
                                    host=DOMAIN_NAME)
        except:
            return 0
    return 0


TITLE = "Felis Catus"
INTRO = "The #1 worst short link redirector, ever."
TABLE_TITLE = "Random "
YEAR = 2020

MAX_RANDOM_COUNT = 5
@app.route('/', methods=['GET'])
def mainView():
    line_count = get_line_count()
    random_count = min(MAX_RANDOM_COUNT, line_count)
    if random_count == 0:
        return render_template('main_empty.tpl', title=TITLE, main_intro=INTRO, table_title=TABLE_TITLE, year=YEAR)
    else:
        TABLE = []
        ints = list(range(1, line_count + 1))
        random.shuffle(ints)
        for v in range(0, random_count):
            i = ints[v]
            peek = __peek(hex(crc32(bytes(str(i), 'utf-8')))[2:].rjust(8, '0'))
            if 'full' in peek:
                TABLE.append(
                    ("#%d" % (i + 1), peek['short'], peek['full'], "./t/%s" % peek['short']))
        return render_template('main.tpl', title=TITLE, main_intro=INTRO, table_title=TABLE_TITLE, table=TABLE, year=YEAR)


def __peek(short_link):
    global conn
    if not conn:
        try:
            conn = psycopg2.connect(database=DB_NAME,
                                    user=USER_NAME,
                                    password=PASSWORD,
                                    host=DOMAIN_NAME)
        except:
            return error_response()
    sql = 'SELECT * FROM "pairs" WHERE short_link = \'{0}\''.format(
        str(short_link))

    print(sql)
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except:
        return error_response()
    response = cur.fetchone()
    cur.close()

    if response and len(response) == 3:
        resp = {
            'short': short_link,
            'full': response[2]
        }
        return resp
    else:
        return error_response()


@app.route('/peek/<short_link>', methods=['GET'])
def Peek(short_link):
    return jsonify(__peek(short_link))


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
