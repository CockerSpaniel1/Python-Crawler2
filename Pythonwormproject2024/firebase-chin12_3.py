from firebase import firebase
firebase = firebase.FirebaseApplication(dsn="https://pythoncrawler-537b3-default-rtdb.firebaseio.com/"
,authentication=None)

result=firebase.get(url="/person", name=None )
len1 = len(result)
keyid = []
for k in result.keys():
    keyid.append(k)

for i in range(0, len1, 1):
    print(keyid[i])
