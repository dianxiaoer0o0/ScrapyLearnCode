# -*- coding: utf-8 -*-
import pymysql
import settings

class mainMethod():
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host=settings.MYSQL_HOST,
                user=settings.MYSQL_USER,
                db=settings.MYSQL_DBNAME,
                passwd=settings.MYSQL_PASSWD,
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

    def execute(self,sql,data=None):
        ans = None
        if data:
            res = self.cur.execute(sql, data)
            if res:
                self.conn.commit()
                ans = self.cur.fetchone()
            else:
                self.conn.rollback()
                print('操作失败')
        else:
            res = self.cur.execute(sql)
            if res:
                ans = self.cur.fetchone()
            else:
                self.conn.rollback()
                print('操作失败')
        return ans[0]

    def dropIP(self,ip):
        sql = r'delete from proxies where proxy=%s'
        res = self.cur.execute(sql,ip)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
            print("删除%s失败"%ip)
        self.close()
    def clearTable(self,tableName):
        sql = r'TRUNCATE TABLE %s'
        self.cur.execute(sql%tableName)
        self.close()

    def get_all(self,tableName):
        sql = r'select * from %s'
        res = self.cur.execute(sql%tableName)
        all_info = self.cur.fetchall()
        self.close()
        return all_info

    def get_movieList(self):
        sql = """select 'name' from movietop250"""
        res = self.cur.execute(sql)
        movieList = self.cur.fetchall()
        self.close()
        return movieList

