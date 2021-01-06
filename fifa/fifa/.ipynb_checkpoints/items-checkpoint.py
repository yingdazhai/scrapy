# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerItem(scrapy.Item):
    # define the fields for fifa players:
    name = scrapy.Field()
    country = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()
    overall_rating = scrapy.Field()
    potential = scrapy.Field()
    club = scrapy.Field()
    value = scrapy.Field()
    wage = scrapy.Field()
    total_stats = scrapy.Field()
    hits = scrapy.Field()
        

