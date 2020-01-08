#!/usr/bin/env python3

import json
import time
import psutil
import random

import psycopg2
import psycopg2.extensions

from zlib import crc32
from flask import jsonify, redirect, render_template, request
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


def __getinfo(cpu_interval=0.1):
    try:
        cpu_pressure = psutil.cpu_percent(cpu_interval)
        cpu_logical_count = psutil.cpu_count()
        cpu_physical_count = psutil.cpu_count(logical=False)

        virtual_mem = psutil.virtual_memory()
        swap_mem = psutil.swap_memory()

        return {
            'status': 'ok',
            'cpu': {
                'pressure': cpu_pressure,
                'logical_core': cpu_logical_count,
                'physical_core': cpu_physical_count
            },
            'virtual_mem': {
                # svmem(total=8589934592, available=2866520064, percent=66.6, used=7201386496, free=216178688, active=3342192640, inactive=2650341376, wired=1208852480)
                'total': virtual_mem[0],
                'available': virtual_mem[1],
                'percent': virtual_mem[2],
                'used': virtual_mem[3],
                'free': virtual_mem[4],
                'active': virtual_mem[5],
                'inactive': virtual_mem[6],
                'wired': virtual_mem[7]
            },
            'swap_mem': {
                # sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)
                'total': swap_mem[0],
                'used': swap_mem[1],
                'free': swap_mem[2],
                'percent': swap_mem[3],
                'sin': swap_mem[4],
                'sout': swap_mem[5]
            }
        }
    except:
        return error_response()


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
    info = __getinfo()
    if info['status'] == 'ok':
        cpu_p = "%d%% (%d logical / %d physical core[s])" % (
            info['cpu']['pressure'], info['cpu']['logical_core'], info['cpu']['physical_core'])
        mem_p = "virtual: %d%% used of %d MiB total; swap: %d%% used of %d MiB total" % (
            info['virtual_mem']['percent'], int(info['virtual_mem']['total'] / (1024 * 1024)), info['swap_mem']['percent'], int(info['swap_mem']['total'] / (1024 * 1024)))
    else:
        cpu_p = '[temporarily unavailable]'
        mem_p = '[temporarily unavailable]'
    line_count = get_line_count()
    random_count = min(MAX_RANDOM_COUNT, line_count)
    if random_count == 0:
        return render_template('main_empty.tpl', title=TITLE, main_intro=INTRO, table_title=TABLE_TITLE, year=YEAR, cpu_pressure=cpu_p, memory_pressure=mem_p)
    else:
        TABLE = []
        ints = list(range(1, line_count + 1))
        random.shuffle(ints)
        for v in range(0, random_count):
            i = ints[v]
            peek = __peek(hex(crc32(bytes(str(i), 'utf-8')))[2:].rjust(8, '0'))
            if peek['status'] == 'ok':
                TABLE.append(
                    ("#%d" % (i + 1), peek['short'], peek['full'], "./t/%s" % peek['short']))
        return render_template('main.tpl', title=TITLE, main_intro=INTRO, table_title=TABLE_TITLE, table=TABLE, year=YEAR, cpu_pressure=cpu_p, memory_pressure=mem_p)


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
            'status': 'ok',
            'short': short_link,
            'full': response[2]
        }
        return resp
    else:
        return error_response()


@app.route('/info', methods=['GET'])
def GetInfo():
    return jsonify(__getinfo())


@app.route('/peek/<short_link>', methods=['GET'])
def Peek(short_link):
    short_link = short_link.replace(' ', '')
    return jsonify(__peek(short_link))


@app.route('/add', methods=['POST'])
def AddNew():
    full_link = request.form.get('full_link')
    global conn
    if not conn:
        try:
            conn = psycopg2.connect(database=DB_NAME,
                                    user=USER_NAME,
                                    password=PASSWORD,
                                    host=DOMAIN_NAME)
        except:
            return jsonify(error_response())

    full_link = full_link.replace(' ', '')
    max_retry = 3
    retry_count = 0
    while retry_count < max_retry:
        try:
            number = get_line_count() + 1
            short_link = hex(crc32(bytes(str(number), 'utf-8'))
                             )[2:].rjust(8, '0')
            sql = "INSERT INTO pairs(short_link, full_link) VALUES ('{0}', '{1}')".format(
                short_link, full_link)
            success_response = {
                'status': 'ok',
                'short_link': short_link,
                'full_link': full_link
            }
            cur = conn.cursor()
            cur.execute(sql)
            return jsonify(success_response)
        except:
            retry_count += 1
            continue
    return jsonify(error_response())


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

    short_link = short_link.replace(' ', '')
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
