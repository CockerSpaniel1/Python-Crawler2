from firebase import firebase
firebase = firebase.FirebaseApplication(dsn="https://pythoncrawler-537b3-default-rtdb.firebaseio.com/"
,authentication=None)

id="p1008"
name="姓名六"
birth="84/07/03"
blood="B"
school="大學"

data2={"id":id,
       "name":name,
       "birth":birth,
       "blood":blood,
       "school":school
       }

firebase.post(url="/person", data=data2 )
print("資料寫入成功")