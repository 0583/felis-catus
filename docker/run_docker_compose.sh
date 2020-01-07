#!/usr/bin/env bash 
docker-compose down
docker pull docker.pkg.github.com/0583/felis-catus/felis-catus-db:latest
docker pull docker.pkg.github.com/0583/felis-catus/felis-catus-server:latest
docker-compose up
