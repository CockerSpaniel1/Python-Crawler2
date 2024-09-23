from pyquery import PyQuery

dom =PyQuery(url = "https://www.google.com.tw/")
links = dom("title")
#print(links)
for i in links.items():
    print(i.text())