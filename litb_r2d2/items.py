# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LitbR2D2Item(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    product_id = scrapy.Field()
    has_color = scrapy.Field()

