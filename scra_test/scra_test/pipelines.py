# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ScraTestPipeline(object):

    def open_spider(self, spider):
        self.file = open('weather.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # self.save_item(item['item_id']+'.txt' , item)
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item

class ScraAqiPipeline(object):

    def open_spider(self, spider):
        self.file = open('aqi.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # self.save_item(item['item_id']+'.txt' , item)
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item

