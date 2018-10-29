#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:02:46 2018

@author: fangyucheng
"""
import cgi
import requests

parameter = cgi.FieldStorage()
url = 'http://www.baidu.com'

get_page = requests.get(url)
text = get_page.text

print("Content-type: text/html\n")
print("<p>follows are got from website: %s</p>" % text)