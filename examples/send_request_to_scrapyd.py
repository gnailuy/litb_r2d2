#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import time
import sys


scrapyd_url = "http://varchbox:6800/"
schedule = "schedule.json"
status = "daemonstatus.json"
max_job = 2

prefix = "http://www.lightinthebox.com/_p"  # + id + '.html'
payload = {
    "project" : "litb_r2d2",
    "spider"  : "product",
    "urls"    : "",
}


def usage(argv):
    print "Usage:"
    print "\t" + argv[0] + " filename"


def get_new_submitted_jobs():
    while True:
        response = requests.get("%s%s" % (scrapyd_url, status))

        if response.status_code == 200:
            j = json.loads(response.text)
            return j.get("running") + j.get("pending")

        time.sleep(5)


def main(argv):
    if len(argv) != 2:
        usage(argv)
        sys.exit(-1)

    filename = argv[1]
    ids = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                ids.append(line)

                if len(ids) >= 50:
                    send_requests(ids)
                    ids = []

        if len(ids) > 0:
            send_requests(ids)


def send_requests(ids):
    while True:
        submitted_jobs = get_new_submitted_jobs()
        if submitted_jobs < max_job:
            break
        time.sleep(10)

    urls = []
    for i in ids:
        urls.append(prefix + i + '.html')
    payload["urls"] = ",".join(urls)
    print payload

    while True:
        response = requests.post("%s%s" % (scrapyd_url, schedule), data=payload)
        if response.status_code == 200:
            print response
            break

        time.sleep(5)


if __name__ == '__main__':
    main(sys.argv)

