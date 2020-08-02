# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class AmazonBestsellersPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='mytestDB')

        self.c = self.conn.cursor()

    def create_table(self):
            self.c.execute(''' DROP TABLE IF EXISTS amazon_best_seller_elec''')
            self.c.execute(''' CREATE TABLE amazon_best_seller_elec (item_name text,
                                        price text,
                                        image varchar(255),
                                        rank1 varchar(10))''')


    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.c.execute(''' INSERT INTO amazon_best_seller_elec VALUES (%s,%s,%s, %s) ''', (
            item['item_name'][0],
            item['price'][0],
            item['image'][0],
            item['rank1'][0]
        ))
        self.conn.commit()