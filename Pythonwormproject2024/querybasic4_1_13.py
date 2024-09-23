from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
# links = dom("#17 a")
#links = dom("#17").children("a")
links = dom("#17").find("a")
lens1 = len(links)

print(lens1)

k=1
for i in links.items():
     if k%3==0:
          print(i.text())
     else:
          print(i.text(), end="\t")
     k+=1

# k=1
# for i in links.items():
#      print(i.text(), end="\t")
#      if k%3==0:
#           print("")
#      k+=1

