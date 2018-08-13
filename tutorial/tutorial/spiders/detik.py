# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy import Request

# import log module
import logging
# config module
logging.basicConfig(filename='example.log',level=logging.DEBUG)


class DetikSpider(scrapy.Spider):
    name = 'detik'
    allowed_domains = ['detik.com']
    start_urls = ['https://www.detik.com/search/searchall?query=kapal+tenggelam']
    
    def parse(self, response):
        # get html full page
        #logging.info(response.text)

        # get href link form query results
        logging.info(response.selector.xpath('//article//a/@href').extract())
