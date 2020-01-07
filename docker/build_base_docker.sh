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


docker push yuxiqian/felis-catus-base

echo "Done"
rm -rf src_tmp