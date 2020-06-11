import pymongo
from bson.objectid import ObjectId

myclient=pymongo.MongoClient(host='127.0.0.1', port=27017)   #指定主机和端口号创建客户端
mydb = myclient["tech_info"]
mycol_1 = mydb["achievement_wrjs_xny"]
mycol_2 = mydb["conference_wrjs_xny"]
mycol_3 = mydb["degree_wrjs_xny"]
mycol_4 = mydb["legislation_wrjs_xny"]
mycol_5 = mydb["patent_wrjs_xny"]
mycol_6 = mydb["periodical_wrjs_xny"]
mycol_7 = mydb["report_wrjs_xny"]
mycol_8 = mydb["standard_wrjs_xny"]

for x in mycol_2.find():
    y = x["_id"]
    mycol_2.update_one({"_id": ObjectId(y)}, {"$set": {"conference_organ": x["conference_organ"].split("／")}})
    mycol_2.update_one({"_id": ObjectId(y)}, {"$set": {"conference_organ": x["conference_organ"].split(";")}})
    mycol_2.update_one({"_id": ObjectId(y)}, {"$set": {"conference_organ": x["conference_organ"].split("、")}})


for x in mycol_4.find():
    y = x["_id"]
    mycol_4.update_one({"_id": ObjectId(y)}, {"$set": {"issuing_department": x["issuing_department"].split("／")}})
    mycol_4.update_one({"_id": ObjectId(y)}, {"$set": {"issuing_department": x["issuing_department"].split(";")}})
    mycol_4.update_one({"_id": ObjectId(y)}, {"$set": {"issuing_department": x["issuing_department"].split("、")}})

for x in mycol_8.find():
    y = x["_id"]
    mycol_8.update_one({"_id": ObjectId(y)}, {"$set": {"organization": x["organization"].split("／")}})
    mycol_8.update_one({"_id": ObjectId(y)}, {"$set": {"organization": x["organization"].split(";")}})
    mycol_8.update_one({"_id": ObjectId(y)}, {"$set": {"organization": x["organization"].split("、")}})