# -*- coding: utf-8 -*-

import random
import re
import scrapy

from litb_r2d2.items import LitbR2D2Item
from scrapy.exceptions import CloseSpider


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["lightinthebox.com"]
    start_urls = []
    http_proxies = []

    def __init__(self, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        if 'urls' not in kwargs:
            raise CloseSpider('Error: urls not provided as parameters!')
        for url in kwargs.get('urls').split(','):
            self.start_urls.append(url)
        if 'proxies' in kwargs:
            for proxy in kwargs.get('proxies').split(','):
                self.http_proxies.append(proxy)

    def parse(self, response):
        item = LitbR2D2Item()

        item['product_id'] = [re.sub(r'\.html', '', response.url.split('_')[-1])]

        color = response.xpath(
            '//form[@class="widget prod-info-order ctr-info"]/ul/li[1]/select[@name="id[545]"]/option/text()'
        ).extract()
        if len(color) > 0:
            item['has_color'] = [True]
        else:
            item['has_color'] = [False]

        return item

    def make_requests_from_url(self, url):
        request = super(ProductSpider, self).make_requests_from_url(url)

        if len(self.http_proxies) > 0:
            request.meta['proxy'] = random.choice(self.http_proxies)
        elif 'proxy' in request.meta:
            del request.meta['proxy']

        return request

