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
    dont_filter=True

    # for parse first
    def parse(self, response):
        # get html full page
        #logging.info(response.text)

        # get href link form query results
        link_href = response.selector.xpath('//article//a/@href').extract()
        for href in link_href :
            logging.info(href)
            yield scrapy.Request(href, callback=self.parse_detail, dont_filter=True)
        # do something for recursives

    # for parse detail news
    # get content article
    def parse_detail(self, response):
        link_href = response.selector.xpath("//article//div//div[contains(@id, 'detikdetailtext')]/text()").extract()
        # show to log
        logging.info(link_href)
