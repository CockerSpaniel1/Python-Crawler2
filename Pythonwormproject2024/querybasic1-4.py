from pyquery import PyQuery
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
xurl = "https://recreation.forest.gov.tw/Forest/RA?typ_id=0300004"
dom = PyQuery(url=xurl)

links = dom("a")

adata =[]
for i in links.items():
    adata.append(i.text())
len1 = len(adata)
print(len1)

