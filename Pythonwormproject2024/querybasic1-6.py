from pyquery import PyQuery
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
xurl = "https://recreation.forest.gov.tw/Forest/RA?typ_id=0300004"
dom = PyQuery(url=xurl)

links = dom(".left_box a")

kdata =[]
for i in links.items():
    kdata.append(i.text())
len1 = len(kdata)
print(len1)

for i in range(0, len1, 1):
    print(kdata[i])

