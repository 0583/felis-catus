#!/usr/bin/env bash 

sudo apt-get update &&
sudo apt-get -y install postgresql libpq-dev &&
echo "host    all             all             127.0.0.1/32            md5" > sudo tee -a /etc/postgresql/9.5/main/pg_hba.conf &&
sudo service postgresql restart && sleep 3 &&
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';" &&
sudo service postgresql restart && sleep 3