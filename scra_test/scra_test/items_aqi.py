# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScraAqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_id = scrapy.Field()
    weather_quality = scrapy.Field()
    weather_aqi = scrapy.Field()
    weather_pm25 = scrapy.Field()
    weather_pm10 = scrapy.Field()
    weather_No2 = scrapy.Field()
    weather_So3 = scrapy.Field()
    weather_Co = scrapy.Field()
    weather_O3 = scrapy.Field()
    url = scrapy.Field()
    pass
