# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.loader import ItemLoader
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
            #提取电影详情页链接
            info_url = movie.xpath('.//div[@class="hd"]/a/@href').extract()[0]
            #提取电影详情
            yield scrapy.Request(info_url,meta={'item':item},callback=self.info_parse,dont_filter=True)
            # #提取电影介绍
            # infos = movie.xpath('.//div[@class = "bd"]/p/text()').extract()
            # fullInfo = ''
            # for info in infos:
            #     fullInfo += info
            # #item['info'] = fullInfo
            # #print(fullInfo)
            # item['director'] = re.search(r'导演:.*\s主演|导演:.*\.{3}',fullInfo).group()[3:-3].strip()
            # item['actors'] = re.search(r'主演.*\.|主演.*\s{20}|\.',fullInfo).group()[4:-3].strip('/').strip().replace('/',',')
            # item['year'] = re.search(r'\d+',fullInfo).group()
            # item['country'] = re.search(r'/.*/',fullInfo).group()[2:-2]
            # item['types'] = re.search(r'/\s[^/]+\s{5}',fullInfo).group()[2:].strip().replace(' ',',')
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

    def info_parse(self,response):
        item = response.meta['item']
        item['director'] = response.xpath('//a[@rel="v:directedBy"]/text()').extract()[0]
        print(item['director'])
        item['actors'] = response.xpath('//a[@rel="v:starring"]/text()').extract()[0]
        item['types'] = response.xpath('//span[@property="v:genre"]/text()')
        item['country'] = re.search(r'制片国家/地区:</span>(.+?)<br/>',response.text).group()[16:-5].strip()
        item['year'] = response.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()[0]
        yield item


