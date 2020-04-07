import pymysql
import redis
import json
import requests


'''
连接Mysql相关操作
'''
conn = pymysql.connect(host = '192.168.24.142', user = 'root', password = 'Zwkj@123Mysql', port = 3306, db = 'clbs',charset = 'utf8')
cur = conn.cursor() #生成游标对象
sql = "select id from zw_m_vehicle_info where brand = '测PL0092' and flag = 1"
cur.execute(sql)
data = cur.fetchall() #获取执行SQL查询到的数据
for i in data[:1]:
    print(i)
cur.close()


'''
连接Redis相关操作
'''

pool = redis.ConnectionPool(host = '192.168.24.142', port = 6379 , password = 'ZwLBs_Redis@8F3!',db = 15) #建立连接池
r = redis.Redis(connection_pool= pool)
result = r.get('15d97856-c454-431d-992b-206e14ddf027-alarming')#获取对应key的value
rs = json.loads(result) #将得到的值从byte类型转换成dict
val = rs["description"]
print(result)
print(type(result))
print(rs)
print(type(rs))
print(val)


login_url = 'http://192.168.24.142:8080/clbs/j_spring_security_check'
login_data = {
    'username': 'jiangtianshi',
    'password': '0000000'
}
s = requests.session()
r = requests.post(url= login_url, data = login_data)

jsession = r.headers['Cookie']
print(jsession)







