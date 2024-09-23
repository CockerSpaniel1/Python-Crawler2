from pyquery import PyQuery

dom = PyQuery(url="https://bugworkshop.blogspot.com/2018/10/diy-esp32esp32_2.html", encoding="utf-8")
links = dom("span")
len1 = len(links)
print(len1)

k=1
p=1
for i in links.items():
    k=k+1
    if (k>=455 and k<=474):
        print(p, ":",end=" ")
        data = i.text()
        print(data)
        p+=1
