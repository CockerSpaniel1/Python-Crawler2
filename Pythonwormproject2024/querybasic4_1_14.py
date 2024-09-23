from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom("#17 a").text()
mydata = links.split(" ")
lens = len(mydata)

print(lens)

k=1
for i in range(0, lens, 1):
     if k%3==0:
          print(mydata[i])
     else:
          print(mydata[i], end="\t")
     k+=1

# k=1
# for i in links.items():
#      print(i.text(), end="\t")
#      if k%3==0:
#           print("")
#      k+=1

