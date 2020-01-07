#!/usr/bin/env bash 

./init_db_as_postgres.sh
./init_link.sh
python ./gen_rb.py
./init_data.sh
