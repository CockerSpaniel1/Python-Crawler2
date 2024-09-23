from pyquery import PyQuery
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

dom = PyQuery(url="https://recreation.forest.gov.tw/Forest/RA?typ_id=0300004")

links = dom("title")

for i in links.items():
    print(i.text())
