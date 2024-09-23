from pyquery import PyQuery
import sqlite3

dom = PyQuery(url="https://www.descato.com/pages/%E7%BE%8E%E5%AE%B9%E7%94%A2%E5%93%81%E8%B3%87%E6%96%99", encoding="utf-8")

links = dom(".CustomPage table tr")
len1 = len(links)

data=links.text()
# print(data)
kdata=data.split("\n")
len1 = len(kdata)
print(kdata[0])
print(kdata[1])
print(kdata[2])
print(kdata[3])
print(kdata[4])


