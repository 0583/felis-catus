#!/usr/bin/env bash 

rm -rf ./src_tmp

cp -r ../src src_tmp

cp ../utils/install_pg_for_docker.sh ./src_tmp/install_pg.sh
cp ../requirements.txt ./src_tmp/requirements.txt

rm -rf ./src_tmp/migrations

echo "Going to build felis-catus-base docker"
cp ./base/Dockerfile ./
docker build -t yuxiqian/felis-catus-base .
rm Dockerfile

docker login docker.pkg.github.com --username yuetsin
docker push docker.pkg.github.com/0583/felis-catus/felis-catus-base:latest

echo "Done"
rm -rf src_tmp