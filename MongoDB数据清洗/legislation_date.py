import pymongo
from bson.objectid import ObjectId

myclient=pymongo.MongoClient(host='127.0.0.1', port=27017)   #指定主机和端口号创建客户端
mydb = myclient["tech_info"]
mycol = mydb["legislation_wrjs_xny"]

for x in mycol.find():
    y = x["_id"]
    date_1 = x["release_date"]
    date_2 = x["start_date"]
    year = date_1[0:4]
    if date_1[4] == "0":
        month = date_1[5]
    else:
        month = date_1[4:6]
    if date_1[6] == "0":
        date = date_1[7]
    else:
        date = date_1[6:8]
    mycol.update_one({"_id": ObjectId(y)}, {"$set": {"release_date": year+"年"+month+"月"+date+"日"}})
    year = date_2[0:4]
    if date_2[4] == "0":
        month = date_2[5]
    else:
        month = date_2[4:6]
    if date_2[6] == "0":
        date = date_2[7]
    else:
        date = date_2[6:8]
    mycol.update_one({"_id": ObjectId(y)}, {"$set": {"start_date": year + "年" + month + "月" + date + "日"}})


