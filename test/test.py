


import  sqlite3

conn = sqlite3.connect("D:/PythonProjects/Spider/FinvizSpider/test/test.db")
cu = conn.cursor()
# cu.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")
#cu.execute("create table finviz (No int primary key,Ticker varchar(10),Company text,Sector text,Industry text,Country varchar(255),MarketCap float,PE	float,Price	float,Change float,Volume int)")
#cu.execute("create table finviz3 (PE float,Volume integer)")#No int primary key,
cu.execute("insert into finviz3 values (?,?)",
                   ("a","aa",))
conn.commit()
conn.close()

"""
item['No'],item['Ticker'],item['Company'],item['Sector'],item['Industry'],item['Country'],
item['MarketCap'],item['PE'],item['Price'],item['Change'],item['Volume']
,item['Ticker'],item['Company'],item['Sector'],item['Industry'],
				item['Country'],item['MarketCap'],item['PE'],item['Price'],item['Change'],
				item['Volume']
"""