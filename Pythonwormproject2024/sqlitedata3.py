from pyquery import PyQuery

dom = PyQuery(url="https://bugworkshop.blogspot.com/2018/10/diy-esp32esp32_2.html", encoding="utf-8")

links = dom("span")
lens = len(links)
print(lens)

k=1
data = []
flag = False
for i in links.items():
    k=k+1
    if (k>=455 and k<=474):
        print(k, ":",end=" ")
        print(i.text())

    if i.text()=="ESP32 技術規格：":
        flag = True
    elif i.text()=="相關網址：":
        flag = False

    if flag:
        print(i.text())

