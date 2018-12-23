# -*- coding: utf-8 -*-
import os
from scrapy import cmdline
print("---------------------更新代理IP----------------------------")
os.system('python proxy.py')
print("---------------------启动爬虫------------------------------")
cmdline.execute("scrapy crawl doubanMovie".split())