# -*- coding: utf-8 -*-
import scrapy


class DetikSpider(scrapy.Spider):
    name = 'detik'
    allowed_domains = ['detik.com']
    start_urls = ['https://detik.com/']

    def parse(self, response):
        pass
