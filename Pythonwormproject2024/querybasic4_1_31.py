import requests
from pyquery import PyQuery

spath  = "http://www.photosharp.com.tw"
dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")

links = dom("#HotProduct img")
lens = len(links)
print(lens)

imgdata = []
for i in links.items():
    k = i.attr("src")
    imgdata.append(k)


lens2 = len(imgdata)
for h in range(0, lens2, 1):
    print(imgdata[h])

print("---------------------------------------------------")

links = dom("#HotProduct").find("ul").children("li")
imgdata = []
for i in links.items():
    img = i.find("img")
    img_src = img.attr.src

    if (img_src!=None):
        imgdata.append(img_src)

lens2 = len(imgdata)
for h in range(0, lens2, 1):
    #filename = imgdata[h].split('/')[-1]
    # r = requests.get(imgdata[h])
    #print(filename)
    print(imgdata[h])




