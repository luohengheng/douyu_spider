# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    nickname = scrapy.Field()
    image_link = scrapy.Field()
    imagePath = scrapy.Field()
