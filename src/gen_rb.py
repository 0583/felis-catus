#!/usr/bin/env bash

from binascii import crc32
from dataset import entries


def buildEntry(short, full):
    return """e = Entry("%s", "%s")
db.session.add(e)
""" % (short, full)


procEntryExit = """
db.session.commit()
exit
"""

with open('./db/inits.rb', 'w') as f:
    for short, full in entries.items():
        f.write(buildEntry(hex(crc32(short))[2:].zfill(8), full))
    f.write(procEntryExit)
