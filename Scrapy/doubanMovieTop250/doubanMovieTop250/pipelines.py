# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.request import urlopen
import os
from doubanMovieTop250 import settings
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
            #print('数据库连接成功！')
            self.cur = self.conn.cursor()
    #下载图片并保存，返回保存路径
    def download_img(self,name,url):
        img = urlopen(url)
        localPath =  settings.IMAGE_DIR+name.replace('/','&').replace(':','-')+'.jpg'
        if not os.path.exists(settings.IMAGE_DIR):
            os.mkdir(settings.IMAGE_DIR)
        if img:
            pass    #测试通过，暂时不启用
            # with open(localPath,'wb') as f:
            #     f.write(img.read())
        else:
            localPath = ''
        return localPath
    def process_item(self, item, spider):
        item['localPath']= self.download_img(item['name'],item['img_url'])
        try:
            self.cur.execute(
                """select * from movieTop250 where img_url = %s""",
                item['img_url']
            )
            if self.cur.fetchone():
                print("%s--已在数据库中"%item['name'])
            else:
                #print("开始写入.......")
                sql = """insert into movietop250
                                    value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                movieInfo = (item['ranking'],
                             item['name'],
                             item['rating'],
                             item['num'],
                             item['quote'],
                             item['director'],
                             item['actors'],
                             item['year'],
                             item['country'],
                             item['types'],
                             item['img_url'],
                             item['localPath'],
                             item['IMDB_url'])
                res = self.cur.execute(sql,movieInfo)
                if res:
                    self.conn.commit()
                    print("%s---成功写入"%item['name'])
                else:
                    self.conn.rollback()
                    print("%s---写入失败"%item['name'])
        except Exception as e:
            print(e)
        return item

