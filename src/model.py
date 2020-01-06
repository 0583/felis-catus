#!/usr/bin/env python


from config import db


class Entry(db.Model):
    unique_id = db.Column(db.Integer(), primary_key=True, index=True)
    short_link = db.Column(db.String(80), unique=True)
    full_link = db.Column(db.String(255))

    def __init__(self, short, full):
        assert(type(short) == str and type(full) == str)
        self.short_link = short
        self.full_link = full

    def __repr__(self):
        return '<Pair #%d: /t/%s>' % (self.unique_id, self.short_link)

    def __str__(self):
        return """
unique id:  %d
short link: %s
full link:  %s
""" % (self.unique_id, self.short_link, self.full_link)
