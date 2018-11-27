#encoding:utf-8
import scrapy

class mingyan(scrapy.Spider):

    name = "mingyan"
    start_urls = [
        'http://lab.scrapyd.cn',
    ]
    def parse(self,response):
        mingyan = response.css('div.quote')
        for item in mingyan:
            text = item.css('.text::text').extract_first()
            author = item.css('.author::text').extract()
            tags = item.css('.tags .tag::text').extract()
            tags = ",".join(tags)

            fileName = '%s-语录.txt' % author[0]
            with open(fileName,'a+') as f:
                f.write(text)
                f.write('\n')
                f.write('标签：' + tags)
                f.write('\n---------------------\n')
        nextPage = response.css('li.next a::attr(href)').extract_first()
        if nextPage is not None:
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage,callback=self.parse)