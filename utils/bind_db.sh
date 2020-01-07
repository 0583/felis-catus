#!/usr/bin/env bash 

./install_pg.sh
./init_db_as_postgres.sh < pswd
./init_link.sh
python ./gen_rb.py
./init_data.sh
