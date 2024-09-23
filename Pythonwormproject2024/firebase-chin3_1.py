from firebase import firebase
firebase = firebase.FirebaseApplication(dsn="https://pythoncrawler-537b3-default-rtdb.firebaseio.com/"
,authentication=None)
firebase.post(url="name2", data="迪麗熱巴" )
print("資料儲存成功")