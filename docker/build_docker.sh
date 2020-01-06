#!/usr/bin/env bash 

echo "Going to build felis-catus-db docker"
cp ./db/Dockerfile ./
docker build -t yuxiqian/felis-catus-db .
rm Dockerfile

echo "Going to build felis-catus-server docker"
cp ./server/Dockerfile ./
docker build -t yuxiqian/felis-catus-server .
rm Dockerfile

echo "Going to push felis-catus-db docker"
docker push yuxiqian/felis-catus-db

echo "Going to push felis-catus-server docker"
docker push yuxiqian/felis-catus-server

echo "Done"