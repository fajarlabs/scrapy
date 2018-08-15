	# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import json
import psycopg2
from tutorial.spiders.postgredb import connectDbAndQuery
from tutorial.spiders.config import config


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
	        line = json.dumps(dict(item)) + "\n"
	        self.file.write(line)
        except Exception as e:
            logging.debug(str(e))

        # save data into database
        conn = None
        try:
			# read connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # set autocommit 
            conn.autocommit = True
            # create a cursor
            cur = conn.cursor()
            # execute a statement
            query = "INSERT INTO scrapy_detik (date,content) VALUES (%s, %s)"
            data = ('a', 'b')
            cur.execute(query, data)
            # commit execute
            conn.commit()
            # close connection
            cur.close()
        except Exception as e:
          logging.debug(str(e))

        return item