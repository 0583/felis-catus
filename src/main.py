#!/usr/bin/env python3

import psycopg2
import psycopg2.extensions

from config import app, db
from consts import DEBUG, PORT
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from model import Entry


migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Entry=Entry)


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))


@app.route('/t/<short_link>', methods=['GET'])
def redirect(short_link):
    if not conn:
        conn = psycopg2.connect(
            database='felisdb', user='felis', password='', host='localhost')
    sql = "SELECT * FROM felisdb WHERE short_link = "


if __name__ == "__main__":
    manager.run()
