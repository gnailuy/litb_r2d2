#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import settings


payload = {
    "project" : settings.BOT_NAME,
    "spider"  : "product",
    "urls"    : "http://www.lightinthebox.com/_p1318511.html, \
                 http://www.lightinthebox.com/_p4850022.html, \
                 http://www.lightinthebox.com/_p351949.html",
    }
response = requests.post("http://varchbox:6800/schedule.json", data=payload)
print response

