# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib
import  scrapy
import  MySQLdb
from scrapy.exceptions import DropItem


test = "D:/PythonProjects/Spider/FinvizSpider/test/test.db"

class JiandanPipeline(object):
    def process_item(self, item, spider):
        cx = sqlite3.connect(test)
        pe = "-"

        if(len(item['PE'])==0):
            pe="-"
        else:
            pe =item['PE'][0]
        volume = item['Volume'][0]

        print pe,volume
        cx.execute("insert into finviz values (?,?,?,?,?,?,?,?,?,?,?)",#,
				(item['No'][0],item['Ticker'][0],item['Company'][0],item['Sector'][0],item['Industry'][0],
				item['Country'][0],item['MarketCap'][0],pe,item['Price'][0],item['Change'][0],
				item['Volume'][0]))
        # cx.execute("insert into finviz values (?,?,?,?,?,?,?,?,?,?,?)",#,
			# 	(str(item['No']),str(item['Ticker'][0]),str(item['Company']),str(item['Sector']),str(item['Industry']),
			# 	str(item['Country']),str(item['MarketCap']),str(item['PE']),str(item['Price']),str(item['Change']),
			# 	str(item['Volume'])))
        cx.commit()
        cx.close()
        return item

class MySqlPipeLine(object):
    def process_item(self, item, spider):
        # 打开数据库连接
        db = MySQLdb.connect("127.0.0.1","root","root","finvizdb" )

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        sql = self.createSql(item)
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # try:
        #    # 执行sql语句
        #    cursor.execute(sql)
        #    # 提交到数据库执行
        #    db.commit()
        # except:
        #    # 发生错误时回滚
        #    db.rollback()

        # 关闭数据库连接
        db.close()

        return  item
    #创建sql
    def createSql(self,item):
        No = 0
        Ticker = ''
        Company = ''
        Sector =''
        Industry = ''
        Country = ''
        MarketCap =''
        PE = 0
        Price = 0
        ChangeV = 0
        Volume = 0

        No =int(item['No'][0])
        Ticker = str(item['Ticker'][0])
        Company =str(item['Company'][0]).replace('\'','\\\'')
        Sector = str(item['Sector'][0])
        Industry = str(item['Industry'][0])
        Country = str(item['Country'][0])


        if(len(item['MarketCap'])==0 or item['MarketCap'][0]=="-"):
            MarketCap ='0'
        else:
            MarketCap = str(item['MarketCap'][0])

        if(len(item['PE'])==0 or item['PE'][0]=='-'):
            PE = 0
        else:
            PE =float(item['PE'][0])
        if(len(item['Price'])==0 or item['Price'][0]=='-'):
            Price = 0
        else:
            Price = float(item['Price'][0])

        if(len(item['ChangeV'])==0 or item['ChangeV'][0]=="-"):
            ChangeV =0
        else:
            ChangeV = float(str(item['ChangeV'][0]).replace('%',''))

        if(len(item['Volume'])==0 or item['Volume'][0]=="-"):
            Volume =0
        else:
            Volume = int(str(item['Volume'][0]).replace(',',''))

        sql = """INSERT INTO `7/29spy500_tradestock`(NO,Ticker,Company,Sector,Industry,Country,MarketCap,PE,Price,ChangeV,Volume)
                            VALUE('%d','%s','%s','%s','%s','%s','%s','%f','%f','%f','%d')"""%\
                (No,Ticker,Company,Sector,Industry,Country,MarketCap,PE,Price,ChangeV,Volume)
               # (item['No'][0],item['Ticker'][0],item['Company'][0],item['Sector'][0],item['Industry'][0],item['Country'][0],MarketCap,pe,item['Price'][0],ChangeV,Volume)
        return sql

