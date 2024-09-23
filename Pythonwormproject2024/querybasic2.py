from pyquery import PyQuery

dom = PyQuery("<html><head><title>網路爬蟲語言</title></head></html>")

links = dom("title")
for i in links.items():
    print(i.text())
