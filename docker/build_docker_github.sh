#!/usr/bin/env bash 

rm -rf ./src_tmp

cp -r ../src src_tmp

cp ../utils/bind_db.sh ./src_tmp/bind_db.sh
cp ../utils/install_pg_for_docker.sh ./src_tmp/install_pg.sh
cp ../requirements.txt ./src_tmp/requirements.txt

rm -rf ./src_tmp/migrations

echo "Going to build felis-catus-db docker"
cp ./db/Dockerfile ./
docker build -t docker.pkg.github.com/0583/felis-catus/felis-catus-db .
rm Dockerfile

echo "Going to build felis-catus-server docker"
cp ./server/Dockerfile ./
docker build -t docker.pkg.github.com/0583/felis-catus/felis-catus-server .
rm Dockerfile

docker login docker.pkg.github.com -u Yuan-Zhuo -p "$ACCESS_TOKEN"
docker push docker.pkg.github.com/0583/felis-catus/felis-catus-db:latest
docker push docker.pkg.github.com/0583/felis-catus/felis-catus-server:latest

echo "Done"
rm -rf src_tmp