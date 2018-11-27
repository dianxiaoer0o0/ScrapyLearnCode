#encoding:utf-8
import scrapy

class mingyan(scrapy.Spider):

    name = "mingyan"
    start_urls = [
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]
    def parse(self,response):
        mingyan = response.css('div.quote')[0]

        text = mingyan.css('.text::text').extract_first()
        author = mingyan.css('.author::text').extract()
        tags = mingyan.css('.tags .tag::text').extract()[0:2]
        tags = ",".join(tags)

        fileName = '%s-语录.txt' % author
        with open(fileName,'w') as f:
            f.write(text)
            f.write('\n')
            f.write('标签：' + tags)
