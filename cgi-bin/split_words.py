#!/usr/bin/python3
"""
Created on Mon Oct 29 10:37:34 2018

@author: fangyucheng
"""


import cgi
import jieba

parameter = cgi.FieldStorage()

sentence = parameter['input'].value

cut_result = jieba.lcut(sentence)

output_words = ','.join(cut_result)

print("Content-type: text/html\n")
print("<TITLE>Cut Result</TITLE>")
print("<H1>your sentence has been cut</H1>")
print("<p>cut_result: %s</p>" % output_words)