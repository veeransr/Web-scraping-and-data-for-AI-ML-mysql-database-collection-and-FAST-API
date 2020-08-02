# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonBestsellersItem(scrapy.Item):
    item_name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    rank1 = scrapy.Field()


