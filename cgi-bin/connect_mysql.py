#!/usr/bin/python3

import cgi
import pymysql
import datetime
import pandas as pd

parameter = cgi.FieldStorage()

re_date = parameter['input'].value

re_date_dt = datetime.datetime.strptime(re_date, '%Y-%m-%d')

next_date_dt = re_date_dt + datetime.timedelta(days=1)

next_date = datetime.datetime.strftime(next_date_dt, '%Y-%m-%d')

search_sql = ("select * from user_performance where create_time >='"
              + re_date + "' and create_time <='" + next_date + "'")

host='host'
user='user'
passwd='passwd'
database_name='crawler_opgg'
port='port'

connection = pymysql.connect(host=host, user=user, passwd=passwd,
                             db=database_name, port=port,
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

print("Content-type: text/html\n")
print("<TITLE>Downloading</TITLE>")
print("<H1>Your requirement has been processed</H1>")
print("<p>connent with database successfully</p>")

cursor.execute(search_sql)
data_lst = cursor.fetchall()[:100]

print("<p>download %s data successfully</p>" % len(data_lst))

df = pd.DataFrame(data_lst)

csv_name = '/var/www/html/' + re_date + '.csv'

df.to_csv(csv_name, index=False, encoding='gb18030')

print("<p>write %s into server</p>" % csv_name)
