from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")

links1 = dom("ul") #soup.select(ul)

lens1 = len(links1) #有幾個ul

k=1
for i in range(0,lens1 ,1):
     links2 = dom("ul").eq(i)
     dom2 = PyQuery(links2)
     links3 = dom2("li")
     lens2 = len(links3) #第i個ul li長度
     print("第[%d]UL元件有[%d]個LI項目" % (k, lens2))

     # for j in range(0 , lens2, 1):
     #      links3.text()
     #      dom3 = PyQuery(links3).eq(j)
     #
     #      for i in links2.items():
     #           print(i.text())
     for j in links3.items():
          print(j.text())
     k=k+1

