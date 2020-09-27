# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    film_name = scrapy.Field()
    film_type = scrapy.Field()
    plan_date = scrapy.Field()
