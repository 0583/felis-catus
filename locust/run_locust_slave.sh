#!/usr/bin/env bash 

locust -f locustfile.py --slave --master-host=$HOST_IP