# encoding:utf-8
import pymysql

class Mysql(object):
    def __init__(self):#创建连接
        try:
            self.conn = pymysql.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                passwd = 'root',
                db = 'testdb',
                charset = 'utf8'
            )
        except Exception as e:
            print(e)
        else:
            print('连接成功')
            self.cur = self.conn.cursor()

    def create_table(self,name,column):#创建表
        sql = """create table %s(%s)""" #想用参数传入，但没找到方法，还是构造字符串
        res = self.cur.execute(sql%(name,column))
        print(res)

    def close(self):#关闭连接
        self.cur.close()
        self.conn.close()

    def add(self,table,value):#增
        sql = """insert into %s values (%s)"""
        res = self.cur.execute(sql%(table,value))
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def rem(self):#删
        sql = """delete from testtb where id = 1"""
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def mod(self):#改
        sql = """update testtb set name = "tom ding" where id = 2"""
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)
    def show(self):#查
        sql = """select * from testtb"""
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
             print(i)
if __name__ == '__main__':
    mysql = Mysql()
    table_name = 'hello'
    column = 'id int,name varchar(10), age int'
    mysql.create_table(table_name,column)
    value = "1,'hah',29"
    mysql.add(table_name,value)
    mysql.mod()
    mysql.rem()
    mysql.show()
    mysql.close()