#!/usr/bin/env bash 

sudo -u postgres createuser -h localhost -p 5432 felis -P < user_pswd
sudo -u postgres createdb -O felis felisdb