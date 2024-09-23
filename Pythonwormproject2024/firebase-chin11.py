from firebase import firebase
firebase = firebase.FirebaseApplication(dsn="https://pythoncrawler-537b3-default-rtdb.firebaseio.com/"
,authentication=None)


while True:
       ch = input("選單(1)新增資料(2)離開:")

       if int(ch) == 2:
              break

       if  int(ch) == 1:
              id = input("輸入編號:")
              name = input("輸入姓名:")
              birth = input("輸入生日:")
              blood = input("輸入血型:")
              school = input("輸入學歷:")


              data2={"id":id,
                     "name":name,
                     "birth":birth,
                     "blood":blood,
                     "school":school
                     }

              firebase.post(url="/person", data=data2 )
              print("資料寫入成功")