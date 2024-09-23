from firebase import firebase
firebase = firebase.FirebaseApplication(dsn="https://pythoncrawler-537b3-default-rtdb.firebaseio.com/"
,authentication=None)

result=firebase.get(url="/person", name=None )
len1 = len(result)
keyid = []
for k in result.keys():
    keyid.append(k)


result2=firebase.get(url="/person/"+keyid[0], name=None )
for t,h  in result2.items():
    print(t, h)
