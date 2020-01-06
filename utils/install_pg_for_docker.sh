#!/usr/bin/env bash 

apt-get update &&
apt-get -y install postgresql libpq-dev &&
echo "host    all             all             127.0.0.1/32            md5" > sudo tee -a /etc/postgresql/9.5/main/pg_hba.conf &&
service postgresql restart && sleep 3 &&
postgres psql -c "ALTER USER postgres PASSWORD 'postgres';" &&
service postgresql restart && sleep 3