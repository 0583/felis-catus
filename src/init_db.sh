#!/usr/bin/env bash 

createuser -h localhost -p 5432 felis
createdb -O felis felis