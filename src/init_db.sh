#!/usr/bin/env bash 

cp ./pg_hba.conf /etc/postgresql/11/main/pg_hba.conf
service postgresql restart
createuser -h localhost -p 5432 felis

sleep 3
createdb -O felis felis