# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScraTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_id = scrapy.Field()
    day_weather = scrapy.Field()
    day_wind = scrapy.Field()
    day_temperature = scrapy.Field()
    night_weather = scrapy.Field()
    night_wind = scrapy.Field()
    night_temperature = scrapy.Field()
    url = scrapy.Field()
    pass
