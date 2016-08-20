# LITB Info Crawler

Run a `scrapyd` server:

    docker run -d --restart always --name scrapyd -v /path/to/litb_r2d2/items:/items -p 6800:6800 vimagick/scrapyd

Deploy to the `scrapyd` server:

    scrapyd-deploy default -p litb_r2d2 --version 1.0

and then send a scrapy job to `scrapyd` via `curl`:

    curl http://hostname:6800/schedule.json -d project=litb_r2d2 -d spider=product -d urls="http://comma.separated.product.urls/"

or via a `python` script:

    python litb_r2d2/send_request_example.py

or via command line without `scrapyd` (be aware that you might not have the write permission of the default output path '/items'):

    scrapy crawl product -a urls='http://comma.separated.product.urls/' -s OUTPUT="/output/path/that/you/have/write/permission"

where `http://hostname:6800/` is the address of the `scrapyd` service, which is also configured in scrapy.cfg as default.

