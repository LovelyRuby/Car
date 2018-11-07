import pymysql
import json
def getCursor(host,user,password,db):
    db = pymysql.connect(host=host,user=user,password=password,db=db,charset="utf8")
    return db.cursor(),db

def insert(carMessage):
    cursor,db = getCursor()
    count = 0
    for i in range(len(carMessage)):
        print(carMessage[i])
        sql = "insert into car (carMessage) value ('{0}')".format(carMessage[i])
        try:
            cursor.execute(sql)
            db.commit()
            count+=1
        except:
            db.rollback()
            print("本条数据插入失败")
    db.close()
    print("共"+str(len(carMessage))+"条数据，成功"+str(count)+"条")

if __name__ == "__main__":
    carMessage = [{"carName": "2016.11.21"},{"carName": "2016.11.21"}]
    print(insert(json.dumps(carMessage)))