#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import settings


payload = {
    "project" : settings.BOT_NAME,
    "spider"  : "product",
    "urls"    : "http://comma.separated.product.urls/",
    }
response = requests.post("http://varchbox:6800/schedule.json", data=payload)
print response

