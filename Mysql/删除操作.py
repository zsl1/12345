import pymysql
#4.删除操作
db= pymysql.connect(host="localhost",user="root",
 	password="root",db="test",port=3306)
 
# 使用cursor()方法获取操作游标
cur = db.cursor()
 
sql_delete ="delete from user where id = %d"
 
try:
	cur.execute(sql_delete % (3))  #像sql语句传递参数
	#提交
	db.commit()
except Exception as e:
	#错误回滚
	db.rollback() 
finally:
	db.close()
