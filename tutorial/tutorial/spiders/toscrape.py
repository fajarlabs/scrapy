# -*- coding: utf-8 -*-
import scrapy
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)


class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        logging.debug('This message should appear on the console')
        logging.info('So should this')
        logging.warning('And this, too')
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)