#!/usr/bin/env bash 

apt-get update
apt-get -y install postgresql sudo expect
echo "host    all             all             127.0.0.1/5432            md5" > tee -a /etc/postgresql/11/main/posgresql.conf
service postgresql restart
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
service postgresql restart &
sleep 5