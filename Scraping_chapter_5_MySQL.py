import pymysql
conn = pymysql.connect(host='localhost', port=3306,user='root',password='daishun123',db='test')
print('连接成功')
conn.close()
