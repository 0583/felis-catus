#!/usr/bin/env bash 

./install_pg.sh
echo "Pg install over"

./init_db_as_postgres.sh < pswd
echo "Init db over"

./init_link.sh
echo "Init link"

python ./gen_rb.py
echo "Rb gen success"

./init_data.sh
echo "Init data"

