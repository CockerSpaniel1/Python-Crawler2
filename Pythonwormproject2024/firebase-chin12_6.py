from firebase import firebase
firebase = firebase.FirebaseApplication(dsn="https://pythoncrawler-537b3-default-rtdb.firebaseio.com/"
,authentication=None)

result=firebase.get(url="/person", name=None )
len1 = len(result)
keyid = []
for k in result.keys():
    keyid.append(k)

for j in range(0, len1, 1):
    result2=firebase.get(url="/person/"+keyid[j], name=None )
    print(result2["id"], result2["name"], result2["birth"], result2["blood"], result2["school"])

