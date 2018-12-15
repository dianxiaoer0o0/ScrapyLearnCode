# -*- coding: utf-8 -*-
import scrapy 
from doubanMovieTop250 import items

#爬取豆瓣电影TOP250的信息
class doubanMovie(scrapy.Spider):
    # 爬虫唯一标识符
    name = 'doubanMovie'
    # 爬取域名
    allowed_domain = ['movie.douban.com']
    # 爬取页面地址
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):

        #print(response.body)
        selector = scrapy.Selector(response)
        movies = selector.xpath('//div[@class = "item"]')
        item = items.Doubanmovietop250Item()

        for movie in movies:
            #提取电影名字
            titles =movie.xpath('.//span[@class = "title"]/text()').extract()
            name = ''
            for title in titles:
                name += title.strip()
            item['name'] = name
            #提取电影介绍
            infos = movie.xpath('.//div[@class = "bd"]/p/text()').extract()
            fullInfo = ''
            for info in infos:
                fullInfo += info
            item['info'] = fullInfo
            #提取电影评分
            item['rating'] = float(movie.xpath('.//span[@class = "rating_num"]/text()').extract()[0].strip())
            #提取电影评价人数
            item['num'] = int(movie.xpath('.//div[@class = "star"]/span[last()]/text()').extract()[0].strip()[:-3])
            #提取电影名言
            quote = movie.xpath('.//span[@class = "inq"]/text()').extract()
            if quote:
                quote = quote[0].strip()
            else:
                quote = ''
            item['quote'] = quote
            #提取电影封面url
            item['img_url'] = movie.xpath('.//img/@src').extract()[0]
            #返回item
            yield item

        #提取下一页
        nextPage = selector.xpath('.//span[@class = "next"]/a/@href').extract()
        if nextPage:
            url = 'https://movie.douban.com/top250' + nextPage[0]
            yield scrapy.Request(url,callback=self.parse)

