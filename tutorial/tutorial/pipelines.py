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

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # try :
	       #  line = json.dumps(dict(item))
	       #  self.file.write(json.loads(line))
        # except Exception as e:
        #     logging.debug(str(e))

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
            query = "INSERT INTO scrapy_detik (date,content,url) VALUES (%s, %s, %s)"
            data = (item["title"], item["content"], item["url"])
            cur.execute(query, data)
            # commit execute
            conn.commit()
            # close connection
            cur.close()
        except Exception as e:
          logging.debug(str(e))

        return item