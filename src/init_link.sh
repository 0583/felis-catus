#!/usr/bin/env bash 

./main.py db init
./main.py db migrate -m "init felisdb for postgres"
./main.py db upgrade