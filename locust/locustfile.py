#!/usr/bin/env python

from zlib import crc32
from random import randint
from locust import HttpLocust, TaskSet, task

HOST_DOMAIN = '12.34.56.78:8080'


class WebsiteTasks(TaskSet):
    short_link = hex(crc32(bytes(str(randint(1, 32), 'utf-8')))
                     )[2:].rjust(8, '0')

    @task(3)
    def get_info(self):
        self.client.get("/info")

    @task(2)
    def rand_short(self):
        self.client.get("/%s" % short_link)

    @task(1)
    def main(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = HOST_DOMAIN
    min_wait = 1000
    max_wait = 5000
