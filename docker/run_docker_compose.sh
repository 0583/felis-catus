#!/usr/bin/env bash 
docker-compose down
docker pull yuxiqian/felis-catus-db
docker pull yuxiqian/felis-catus-server
docker-compose up
