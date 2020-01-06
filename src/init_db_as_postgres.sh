#!/usr/bin/env bash 

sudo -u postgres createuser -h localhost -p 5432 felis
sudo -u postgres createdb -O felis felisdb