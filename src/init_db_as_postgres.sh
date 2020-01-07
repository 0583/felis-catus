#!/usr/bin/env bash 
expect ./init_db_as_postgres_expect.sh

sudo -u postgres createdb -O felis felis