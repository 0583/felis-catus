#!/usr/bin/env bash 

rm -rf ./src_tmp

cp -r ../src src_tmp

cp ../utils/bind_db.sh ./src_tmp/bind_db.sh
cp ../utils/install_pg_for_docker.sh ./src_tmp/install_pg.sh
cp ../requirements.txt ./src_tmp/requirements.txt

rm -rf ./src_tmp/migrations

echo "Going to build felis-catus-db docker"
cp ./db/Dockerfile ./
docker build -t yuxiqian/felis-catus-db .
rm Dockerfile

echo "Going to build felis-catus-server docker"
cp ./server/Dockerfile ./
docker build -t yuxiqian/felis-catus-server .
rm Dockerfile

docker login -u yuxiqian -p "$DOCKERHUB_TOKEN"
echo "Going to push felis-catus-db docker"
docker push yuxiqian/felis-catus-db

echo "Going to push felis-catus-server docker"
docker push yuxiqian/felis-catus-server
echo "Done"
rm -rf src_tmp