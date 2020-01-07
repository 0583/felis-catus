#!/usr/bin/env bash 

service postgresql restart

./main.py shell < ./db/inits.rb