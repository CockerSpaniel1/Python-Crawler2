from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links1 = dom("ul") #定位ul
lens1 = len(links1)

k=1
for i in range(0,lens1 ,1):
     links2 = dom("ul").eq(i) #選到第i個ul
     dom2 = PyQuery(links2) #PyQuery物件
     links3 = dom2("li")  #定位li
     lens2 = len(links3)
     print("第[%d]UL元件有[%d]個LI項目" % (k, lens2))
     k=k+1

