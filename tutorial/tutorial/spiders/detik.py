# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy import Request
from tutorial.spiders.postgredb import connectDbAndQuery
from urllib.parse import urlparse

# import log module
import logging
# config module
logging.basicConfig(filename='example.log',level=logging.DEBUG)


class DetikSpider(scrapy.Spider):
    name = 'detik'
    allowed_domains = ['detik.com']
    start_urls = ['https://www.detik.com']
    dont_filter=True

    def __init__(self):
        self.content_disallowed = ['#','/']
        self.nodes = 0;
        self.max_nodes = 4

    # for parse first
    def parse(self, response):

        # yield seperti return tapi lebih dari return, yield bisa mengembalikan
        # data yang sedang di proses pada iterasi / perulangan
        # contoh kode di link berikut http://www.adiputra.web.id/generator-yield-pada-python/
        # yield ini diproses oleh pipelines
        # sebelumnya diedit terlebih dahulu pada file settings.py
        # ITEM_PIPELINES = {
        #    'tutorial.pipelines.TutorialPipeline': 300,
        # }

        try :
            link_href = response.selector.xpath('//a/@href').extract()
            for href in link_href :
                
                # filter url yang tidak boleh diakses
                if(self.if_exist(href) == True):
                    continue

                if(self.nodes > (self.max_nodes-1)):
                    # reset nodes
                    self.nodes = 0
                    continue

                # check if Missing scheme // is exist
                try :                    
                    if(href[:2] == '//'):
                        href = 'https:' + href
                    # penggunaan dont_filter https://doc.scrapy.org/en/latest/topics/request-response.html
                    o = urlparse(str(href))
                    if o.path.count('/') > 2:
                        yield scrapy.Request(href, callback=self.parse_detail, dont_filter=True)
                    else :
                        # call again for detail url
                        yield scrapy.Request(href, callback=self.parse, dont_filter=True)
                except Exception as e :
                    logging.debug(str(e))
                finally:
                    self.nodes += 1

        except Exception as e :
            logging.debug(str(e))

    # for parse detail news
    # get content article
    def parse_detail(self, response):
        title = self.filter_eschar(response.selector.xpath("//title/text()").extract())
        content = self.filter_eschar(response.selector.xpath("//article//div//div[contains(@id, 'detikdetailtext')]/text()").extract())
        datetime = self.filter_eschar(response.selector.xpath("//article//div//div[contains(@class, 'date')]/text()").extract())
        if content != "" :
            yield {'title':title,'content':content,'datetime':datetime,'url':str(response.request.url)}

    # filter escape character
    def filter_eschar(self,content):
        if isinstance(content, list):
            content = ' '.join(content)
            return content.replace('\n','').replace('\t','').strip()
        else:
            return content.replace('\n','').replace('\t','').strip()

    # filter content url
    def if_exist(self, content):
        try :
            for p in self.content_disallowed :
                if(p == content):
                    return True
        except Exception as e :
            logging.debug(str(e))
        return False
