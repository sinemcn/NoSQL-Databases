import pymongo
from bson.objectid import ObjectId 

myclient = pymongo.MongoClient("mongodb+srv://sinemcan1:EaYbRpsdNraof7P8@cluster0.0mfpe.mongodb.net/<dbname>?retryWrites=true&w=majority")

mydb = myclient["node-app"]

mycollection = mydb["products"]

# delete_one(): Bir kayıt silebilmek için kullanılır.
# delete_many(): Birden fazla kayıt silebilmek için kullanılır.

for i in mycollection.find():
     print(i)

print('*'*50)

# mycollection.delete_one({"name":"Iphone 7"})

mycollection.delete_many({"name": {"$regex":"^S"}})

for i in mycollection.find():
     print(i)