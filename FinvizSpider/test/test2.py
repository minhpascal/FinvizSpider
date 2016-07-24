
#encoding:utf-8
import  MySQLdb

 # 打开数据库连接
db = MySQLdb.connect("127.0.0.1","root","root","finvizdb" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("create table data (No int primary key,Ticker varchar(10),Company text,Sector text,Industry text,Country varchar(255),MarketCap float,PE	float,Price	double,Change double,Volume int")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
db.close()