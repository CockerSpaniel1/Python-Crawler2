from pyquery import PyQuery
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
xurl = "https://recreation.forest.gov.tw/Forest/RA?typ_id=0300004"
imgurl = "https://recreation.forest.gov.tw"
dom = PyQuery(url=xurl)

#links = dom("div.park a img")
links = dom(".thumb .img_block img")
alts =[]
srcs = []

for i in links.items():
    alts.append(i.attr.alt)
    srcs.append(imgurl+ i.attr.src)


len1 = len(srcs)
print(len1)

p=1
for k in range(0, len1, 1):
    print("%d:%s[%s]" % (p, alts[k], srcs[k]))
    p += 1

