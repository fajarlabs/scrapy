# -*- coding: utf-8 -*-
import scrapy


class DetikSpider(scrapy.Spider):
    name = 'detik'
    allowed_domains = ['detik.com']
    start_urls = ['http://detik.com/']

    def parse(self, response):
        pass
