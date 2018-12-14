# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubanmovietop250Item(scrapy.Item):
    # define the fields for your item here like:
    # 电影名
    name = scrapy.Field()
    # 电影信息
    info = scrapy.Field()
    # 电影评分
    rating = scrapy.Field()
    # 电影评论人数
    num = scrapy.Field()
    # 电影经典语句
    quote = scrapy.Field()
    # 电影图片链接
    image_url = scrapy.Field()
