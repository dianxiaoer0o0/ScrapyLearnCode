# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubanmovietop250Item(scrapy.Item):
    # define the fields for your item here like:

    #电影排名
    ranking = scrapy.Field()
    # 电影名
    name = scrapy.Field()
    ## 电影信息
    #info = scrapy.Field()
    # 电影评分
    rating = scrapy.Field()
    # 电影评论人数
    num = scrapy.Field()
    # 电影经典语句
    quote = scrapy.Field()
    # 电影图片链接
    img_url = scrapy.Field()
    # 电影图片本地路径
    localPath = scrapy.Field()
    # 电影导演
    director = scrapy.Field()
    # 电影主演
    actors = scrapy.Field()
    # 电影出品年
    year = scrapy.Field()
    # 电影出品地区
    country = scrapy.Field()
    # 电影类型
    types = scrapy.Field()
    # IMDB链接
    IMDB_url = scrapy.Field()
