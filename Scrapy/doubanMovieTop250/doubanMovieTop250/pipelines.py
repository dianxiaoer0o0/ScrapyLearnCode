# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import Scrapy.doubanMovieTop250.doubanMovieTop250.settings as settings
import pymysql
class Doubanmovietop250Pipeline(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host = settings.MYSQL_HOST,
                user = settings.MYSQL_USER,
                db = settings.MYSQL_DBNAME,
                passwd = settings.MYSQL_PASSWD,
                charset = 'utf8',
                use_unicode = True
            )
        except Exception as e:
            print(e)
        else:
            print('数据库连接成功！')
            self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        try:
            pass
        except Exception as e:
            print(e)
        return item

