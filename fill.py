import sqlite3
import datetime
import random
def ins(id,photo,date,hour,hash,duration,json):
    connect = sqlite3.connect('cam.db')
    cursor = connect.cursor()
    insert = """INSERT INTO Novaya
                              (id, photo, date, hour, 'id-hash', duration, json)
                              VALUES (?,?,?,?,?,?,?);"""
    tup = (id,photo,date,hour,hash,duration,json)
    cursor.execute(insert,tup)
    connect.commit()
    cursor.close()
    connect.close()
dt = datetime.date(2021,10,26)


for i in range(3, 900):
    js = "{'person in':%s, 'person out':%s, 'bicycle in':%s,'bicycle out':%s,'car':%s,'motorbike':%s,'bus forward':%s,'truck above':%s}" %(random.randint(1,1000),random.randint(1,1000),random.randint(1,1000),random.randint(1,1000),random.randint(1,1000),random.randint(1,1000),random.randint(1,1000),random.randint(1,1000))
    if i%24 == 0 :
        dt+=datetime.timedelta(days=1)
    a = i%24
    ins(i,'photo',dt,a,'efefefesf',60,js)
