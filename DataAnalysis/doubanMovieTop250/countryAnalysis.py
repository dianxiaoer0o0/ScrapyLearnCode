# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pymysql

class myData():

    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user= 'root',
                db= 'douban',
                passwd= 'root',
                charset='utf8',
                use_unicode=True
            )
        except Exception as e:
            print(e)
        else:
            #print('数据库连接成功！')
            self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def get_all(self,tableName = 'movietop250'):
        sql = 'select * from %s'%tableName
        movie_info = pd.read_sql(sql,con=self.conn)
        self.close()
        return movie_info



movieData = myData()
movies=movieData.get_all()
x=movies['director'].value_counts()
x[:10].plot(kind='barh',rot=0)
plt.show()
import matplotlib
print(matplotlib.matplotlib_fname())