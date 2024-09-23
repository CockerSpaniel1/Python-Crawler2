from firebase import firebase
firebase = firebase.FirebaseApplication(dsn="https://pythoncrawler-537b3-default-rtdb.firebaseio.com/"
,authentication=None)
name=firebase.get(url="name2", name=None )
print("姓名:%s" %name)