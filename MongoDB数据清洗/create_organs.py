import pymongo
from bson.objectid import ObjectId

myclient=pymongo.MongoClient(host='127.0.0.1', port=27017)   #指定主机和端口号创建客户端
mydb = myclient["tech_info"]
mycol = mydb["organs"]
mycol_1 = mydb["achievement_wrjs_xny"]
mycol_2 = mydb["conference_wrjs_xny"]
mycol_3 = mydb["degree_wrjs_xny"]
mycol_4 = mydb["legislation_wrjs_xny"]
mycol_5 = mydb["patent_wrjs_xny"]
mycol_6 = mydb["periodical_wrjs_xny"]
mycol_7 = mydb["report_wrjs_xny"]
mycol_8 = mydb["standard_wrjs_xny"]

for x in mycol_1.find():
    for y in x["organs"]:
        mycol.insert_one({"name": y})

for x in mycol_2.find():
    for y in x["conference_organ"]:
        mycol.insert_one({"name": y})

for x in mycol_3.find():
    y = x["organ"]
    mycol.insert_one({"name": y})

for x in mycol_4.find():
    for y in x["issuing_department"]:
        mycol.insert_one({"name": y})

for x in mycol_6.find():
    for y in x["author_organ"]:
        mycol.insert_one({"name": y})

for x in mycol_7.find():
    for y in x["author_organ"]:
        mycol.insert_one({"name": y})

for x in mycol_8.find():
    for y in x["organization"]:
        mycol.insert_one({"name": y})