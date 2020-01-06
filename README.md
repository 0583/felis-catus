# felis-catus
~~British Shorthair~~

Short Link Redirector

[![Build Status](https://msbiglawgood.visualstudio.com/Felis%20Catus/_apis/build/status/0583.felis-catus?branchName=master)](https://msbiglawgood.visualstudio.com/Felis%20Catus/_build/latest?definitionId=3&branchName=master)

## tech stack

* Flask

* PostgreSQL

* ...

## local config

* download & install postgresDB from [here](https://postgresapp.com/downloads.html)

* install requirements at `./requirements.txt`

* run script `./src/init_db.sh` to initialize DB

* run script `./src/init_link.sh` to link DB to flask

* run script `./src/gen_rb.py` to build ruby files
    > skip this step if `./src/dataset.py` isn't modified

* run script `./src/init_data.sh` to push data entries

* run script `./src/run_server.sh` to start the server
