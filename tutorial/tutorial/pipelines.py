	# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import json

# config module
logging.basicConfig(filename='example.log',level=logging.DEBUG)

class TutorialPipeline(object):

    def open_spider(self, spider):
        self.file = open('pipeline.log', 'w')
        logging.info('tutorial pipeline open spider')

    def close_spider(self, spider):
        self.file.close()
        logging.info('tutorial pipeline close spider')

    def process_item(self, item, spider):
    	try :
    		self.file.write(str(item))
    	except Exception as e:
    		logging.debug(str(e))
    	return item
