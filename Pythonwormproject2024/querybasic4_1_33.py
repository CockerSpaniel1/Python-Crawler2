import requests
from pyquery import PyQuery

spath  = "http://www.photosharp.com.tw"
dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")

links = dom("#HotProduct img")
lens = len(links)
#print(lens)

imgdata = []
for i in links.items():
    k = i.attr("src")
    imgdata.append(k)


lens2 = len(imgdata)
for h in range(0, lens2, 1):
    print(imgdata[h])

h=1
for j in range(0, lens2, 1):
    r = requests.get(imgdata[j])
    f = open("image0/chin"+str(h)+".jpg", 'wb')
    for chunk in r.iter_content(chunk_size=512*1024):
        if chunk:
            f.write(chunk)
    f.close()
    h += 1



print("---------------------------------------------------")
links = dom("#HotProduct").find("ul").children("li")
imgdata = []
for i in links.items():
    img = i.find("img")
    img_src = img.attr.src

    if (img_src!=None):
        imgdata.append(img_src)

lens2 = len(imgdata)
j = 1
for h in range(0, lens2, 1):
    imgurl = imgdata[h].split('/')
    print(imgurl)
    filename = imgurl[-1]
    index = filename.find("_")
    jpg = filename.find(".jpg")
    gif = filename.find(".gif")
    png = filename.find(".png")
    if index != -1:
        filename = filename[:index]

        if jpg != -1:
            filename += ".jpg"
        elif gif != -1:
            filename += ".gif"
        elif png != -1:
            filename += ".png"

    imgurl[-1] = filename
    url = '/'.join(imgurl)
    print(url)
    print("---------------------------")

    r = requests.get(url)

    f = open("image0/"+ str(j) +filename[-4:], 'wb')
    for chunk in r.iter_content(chunk_size=512*1024):
         if chunk:
             f.write(chunk)
    f.close()
    j += 1