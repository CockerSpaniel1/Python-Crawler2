from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom(".selectBox")
lens = len(links)
print(lens)

# for i in links.items():
#     print( len( i.find("option") ) )

for d in range(0, lens, 1):
    dom2 = PyQuery(links)
    links2 = dom2(".selectBox")[d]
    lens2 =len(links2)
    dom3=PyQuery(links2)
    links3 = dom3("select").children("option")
    lens3=len(links3)
    print(lens3)
