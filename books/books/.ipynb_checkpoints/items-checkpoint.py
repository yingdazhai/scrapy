# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for our books info:
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    desc = scrapy.Field()
    upc = scrapy.Field()
    avail = scrapy.Field()
    stock = scrapy.Field()
    nreview = scrapy.Field()

