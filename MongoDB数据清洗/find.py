import pymongo
from bson.objectid import ObjectId

myclient=pymongo.MongoClient(host='127.0.0.1', port=27017)   #指定主机和端口号创建客户端
mydb = myclient["tech_info"]
mycol = mydb["keywords"]

for x in mycol.find():
    print(x["key_word"])