#!/usr/bin/env bash 

apt-get update
apt-get -y install postgresql sudo
echo "host    all             all             127.0.0.1/32            md5" > tee -a /etc/postgresql/9.5/main/pg_hba.conf
service postgresql restart
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
service postgresql restart