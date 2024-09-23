from pyquery import PyQuery
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
xurl = "https://recreation.forest.gov.tw/Forest/RA?typ_id=0300004"
dom = PyQuery(url=xurl)

links = dom(".left_box a")

text =[]
titles = []
for i in links.items():
    text.append(i.text())
    titles.append(i.attr.title)


len1 = len(text)
p=1
for k in range(0, len1, 1):
    print("%d:%s[%s]" % (p, text[k], titles[k]) )
    p += 1

for k in range(0, len1, 1):
    try:
        f = open("jungdb6.txt", "a")
        kdata = text[k] + "===>" +titles[k]
        f.write(kdata+"\r\n")
        print("%s" % "資料寫入成功")
        f.close()


    except:
        print("資料寫入失敗")
