#!/usr/bin/env bash 

sudo -u postgres createuser -h localhost -p 5432 --username felis --password 123456
sudo -u postgres createdb -O felis felisdb