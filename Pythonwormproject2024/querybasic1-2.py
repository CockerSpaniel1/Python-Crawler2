from pyquery import PyQuery
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
xurl = "https://recreation.forest.gov.tw/Forest/RA?typ_id=0300004"
dom = PyQuery(url=xurl)

links = dom("img")

images =[]
for i in links.items():
    images.append(i.attr.src)
len1 = len(images)
print(len1)
for img in images:
    url = "https://recreation.forest.gov.tw"+img
    print(url)

#"https://recreation.forest.gov.tw/Files/Forest/RA/photo/trail/0300004/0300004004.jpg"
#"https://recreation.forest.gov.tw/image/icon/web-logo/30uu-logotype-primary.svg"