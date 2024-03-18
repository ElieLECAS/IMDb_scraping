# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MovieItem(scrapy.Item):

    title = scrapy.Field()
    # score = scrapy.Field()
    # genre = scrapy.Field()
    year = scrapy.Field()
    # duration = scrapy.Field()
    # description = scrapy.Field()
    # actors = scrapy.Field()
    # public = scrapy.Field()
    # country =scrapy.Field()