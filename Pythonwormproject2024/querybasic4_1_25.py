import requests
from pyquery import PyQuery

spath  = "http://www.photosharp.com.tw"
dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom("script")
lens = len(links)
jsdata = []
print(lens)

for i in links.items():
    k = i.attr.src
    if (k!=None):
        allpath = spath+i.attr("src")
        jsdata.append(allpath)

lens2 = len(jsdata)
for k in range(0, lens2, 1):
    print(jsdata[k])

for j in range(0, lens2-4, 1):
    filename= jsdata[j].split('/')[-1]
    r = requests.get(jsdata[j])
    f = open("js/"+filename, 'wb')
    for chunk in r.iter_content(chunk_size=512*1024):
        if chunk:
            f.write(chunk)
    f.close()


