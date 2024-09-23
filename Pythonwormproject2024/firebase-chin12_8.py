from firebase import firebase
firebase = firebase.FirebaseApplication(dsn="https://pythoncrawler-537b3-default-rtdb.firebaseio.com/"
,authentication=None)

qname = input("請輸入欲查詢姓名:")

result=firebase.get(url="/person", name=None )
len1 = len(result)
keyid = []
for k in result.keys():
    keyid.append(k)


# for t,h  in result.items():
#     if ch== h['id']:
#         result2 = h
#         print(result2["id"], result2["name"], result2["birth"], result2["blood"], result2["school"])

for j in range(0, len1, 1):
    result2=firebase.get(url="/person/"+keyid[j], name=None )
    tname = result2["name"]
    if tname==qname:
        print(result2["id"], result2["name"], result2["birth"], result2["blood"], result2["school"])

