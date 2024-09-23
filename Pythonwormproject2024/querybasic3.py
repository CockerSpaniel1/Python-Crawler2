from pyquery import PyQuery

dom = PyQuery(url="http://192.168.0.68/Helloproject1/public_html/query1.html")

links = dom("a")
for i in links.items():
    print(i.text(), i.attr.href)
