# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyInfo(scrapy.Item):
    name = scrapy.Field()
    floor = scrapy.Field()
    price_rent = scrapy.Field()
    price_admin = scrapy.Field()
    price_deposit = scrapy.Field()
    price_gratuity = scrapy.Field()
    floor_plan = scrapy.Field()
    floor_area = scrapy.Field()