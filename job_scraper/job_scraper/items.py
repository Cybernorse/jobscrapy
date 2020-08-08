# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    titles=scrapy.Field()
    status=scrapy.Field()
    job_urls=scrapy.Field()
    companies=scrapy.Field()
    days_ago=scrapy.Field()
    salaries=scrapy.Field()
    short_description=scrapy.Field()
    
    
