#!/usr/bin/env bash 

./main.py db init
./main.py db migrate -m "init felis for postgres"
./main.py db upgrade