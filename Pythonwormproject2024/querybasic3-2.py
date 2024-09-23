from pyquery import PyQuery
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
xurl = "https://recreation.forest.gov.tw/Forest/RA?typ_id=0300004"
dom = PyQuery(url=xurl)

links = dom(".left_box a")

text =[]
title = []
for i in links.items():
    text.append(i.text())
    title.append(i.attr.title)


len1 = len(text)
p=1
for k in range(0, len1, 1):
    print("%d:%s[%s]" % (p, text[k], title[k]) )
    p += 1
