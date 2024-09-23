from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom(".selectBox #SubCate").find("option")

lens = len(links)
print(lens)

for i in links.items():
      print(i.text())

#----------方法二-----------------------------------
links2=dom(".selectBox").eq(1).find("select").find("option")

print(len(links2))

for j in links2.items():
     print(j.text())

#----------方法三-----------------------------------
dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links3 = dom(".selectBox").find("#SubCate")
lens = len(links3)
print(lens)

dom2=PyQuery(links3)
link4 = dom2("select").children("option")
lens2 = len(link4)
print(lens2)

for j in links.items():
     print(j.text())