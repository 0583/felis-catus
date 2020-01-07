#!/usr/bin/env bash 
docker-compose down
docker pull yuxiqian/felis-catus-db:latest
docker pull yuxiqian/felis-catus-server:latest
docker-compose up
