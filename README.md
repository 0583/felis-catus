# felis-catus
~~British Shorthair~~

Short Link Redirector

## local config
* download & install postgresDB from [here](https://postgresapp.com/downloads.html)
* install requirements at `./src/requirements.txt`
* run script `./psql/init_db.sh` to initialize DB
* run script `./src/init_link.sh` to link DB to flask
* run script `./src/gen_rb.py` to build ruby files
    > skip this step if `./src/dataset.py` isn't modified
* run script `./src/init_data.sh` to push data entries
