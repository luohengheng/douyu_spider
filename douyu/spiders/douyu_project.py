# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem

class DouyuProjectSpider(scrapy.Spider):
    name = 'douyu_project'
    allowed_domains = ['capi.douyucdn.cn']

    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=10&offset='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        data = json.loads(response.text)['data']
        for each in data:
            item = DouyuItem()
            item['nickname'] = each['nickname']
            item['image_link'] = each['vertical_src']

            yield item

        if self.offset < 40:
            self.offset += 10

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)