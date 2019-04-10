# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time


class AlibabaPipeline(object):
    def process_item(self, item, spider):
        path = os.path.dirname(os.path.abspath(__file__))
        if os.path.exists(path):
            with open('NingboYusingLighting.txt', 'ab') as f:
                f.write((str(int(item['time'])) + ' ' + item['ranking_list_num'] + '\n').encode('utf-8'))
        else:
            os.makedirs(path)
        return item
