# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JiandanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    No = scrapy.Field()
    Ticker = scrapy.Field()
    Company = scrapy.Field()
    Sector = scrapy.Field()
    Industry = scrapy.Field()
    Country = scrapy.Field()
    MarketCap = scrapy.Field()
    PE = scrapy.Field()
    Price = scrapy.Field()
    ChangeV = scrapy.Field()
    Volume = scrapy.Field()
    #images = scrapy.Field()
	#No int primary key,Ticker varchar(10),Company text,Sector text,Industry text,
	#Country text,MarketCap float,PE	float,Price	float,Change float,Volume int
