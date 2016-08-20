# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import re
import time
from scrapy.exceptions import DropItem


def strip_string_in_list(string_list):
    if isinstance(string_list, list):
        striped_list = []
        for v in string_list:
            striped_list.append(strip_string_in_list(v))
        return striped_list
    elif isinstance(string_list, basestring):
        return ' '.join(re.sub(r'[()\[\]{}\'"`\b\f\n\r\t\\]', ' ', string_list).strip().split())
    else:
        return string_list


class DataCleansingPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'product' and 'product_id' in item and len(item['product_id']) == 0:
            raise DropItem('Product not available!')

        for k, vs in item.items():
            item[k] = strip_string_in_list(vs)
        item['date'] = [time.strftime("%Y-%m-%d")]

        return item


class WriteJsonPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        output_path = settings.get("OUTPUT")
        if not output_path:
            output_path = "/items"
        return cls(output_path)

    def __init__(self, output_path):
        self.file = open('%s/items-%s.json' % (output_path, int(time.time())), 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)).decode('unicode-escape').encode('utf-8') + "\n"
        self.file.write(line)

        return item

