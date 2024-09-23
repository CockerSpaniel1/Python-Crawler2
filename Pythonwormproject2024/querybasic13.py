from pyquery import PyQuery

dom = PyQuery(url="http://192.168.0.68/Helloproject1/public_html/query5.html", encoding="utf-8")
links = dom("#list1")
print(links)
item=links.parent()
print(item)
print(item.attr("id"))
