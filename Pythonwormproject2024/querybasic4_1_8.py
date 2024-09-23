from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom("#-1 a")
lens = len(links)
print(lens)
p=1
k=1
print(f"第[%d]組產品" % k)
for i in links.items():
     if (p%3)==0:
          print(p, i.text())
          if(p<lens):
               k += 1
               print(f"第[%d]組產品" % k)
     else:
          print(p, i.text())
     p=p+1

# p=1
# j=1
# for i in links.items():
#      if p%3 == 1:
#           print(f"第{j}組產品")
#           j+=1
#      print(p, i.text())
#      p += 1

# for i in range(0,lens ,1):
#      if i%3 == 0:
#           print(f"第 {j} 組產品")
#           j +=1
#      print(i+1, links[i].text)
#
