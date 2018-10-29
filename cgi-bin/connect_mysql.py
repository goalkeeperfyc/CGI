#!/usr/bin/python3

import cgi
import pymysql
import datetime

parameter = cgi.FieldStorage()

re_date = parameter['input'].value

re_date_dt = datetime.datetime.strftime(re_date, '%Y-%m-%d')

next_date_dt = re_date_dt + datetime.timedelta(days=1)

next_date = datetime.datetime.strptime(next_date_dt, '%Y-%m-%d')

search_sql = ("select * from user_info where create_time >='"
              + re_date + "' and create_time <='" + next_date + "'")

host='172.21.0.17',
user='root',
passwd='goalkeeper@1', 
database_name='crawler_opgg',
port=3306

connection = pymysql.connect(host=host, user=user, passwd=passwd,
                             db=database_name, port=port,
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

print("Content-type: text/html\n")
print("<TITLE>Downloading</TITLE>")
print("<H1>Your requirement has been processed</H1>")
print("<p>connent with database successfully</p>")

cursor.execute(search_sql)
data_lst = cursor.fetchall()[:10]

print("<p>download %s data successfully</p>")
