# felis-catus
~~British Shorthair~~

Short Link Redirector

[![Build Status](https://msbiglawgood.visualstudio.com/Felis%20Catus/_apis/build/status/0583.felis-catus?branchName=master)](https://msbiglawgood.visualstudio.com/Felis%20Catus/_build/latest?definitionId=3&branchName=master)
[![Actions Status](https://github.com/0583/felis-catus/workflows/Docker%20Image%20Build/badge.svg)](https://github.com/0583/felis-catus/actions)

## tech stack

* Flask

* PostgreSQL

* Docker Compose

* Kong

* ...

## local config

* download & install postgresDB from [here](https://postgresapp.com/downloads.html) or with [shell script](https://github.com/0583/felis-catus/tree/master/utils/install_pg.sh)

* install requirements at `./requirements.txt`

* run script `./src/init_db.sh` to initialize DB

* run script `./src/init_link.sh` to link DB to flask

* run script `./src/gen_rb.py` to build ruby files
    > skip this step if `./src/dataset.py` isn't modified

* run script `./src/init_data.sh` to push data entries

* run script `./src/run_server.sh` to start the server

## single-server config

* download & install docker and docker-compose on a web server

* `cd ./docker` and `./run_docker_compose.sh` to bump up the docker composite containers

## cluster config

~~WIP~~ no longer
