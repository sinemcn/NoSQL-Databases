import pymongo
from bson.objectid import ObjectId 

myclient = pymongo.MongoClient("mongodb+srv://sinemcan1:EaYbRpsdNraof7P8@cluster0.0mfpe.mongodb.net/<dbname>?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# update_one() : Sadece bir kaydı güncellemek için kullanılır.Eğer istenilen kriterde birden fazla kayıt varsa bulduğu ilk kaydı günceller.
# update_many(): Birçok kaydı güncellemek için kullanılır.Eğer istenilen kriterde birden fazla kayıt varsa tüm kayıtları günceller.

# mycollection.update_one(
#     {'name': 'Iphone 12 Pro Max'},
#     {'$set':{
#          'name':'Samsung S20 Plus',
#          'price': 15500
#     }}
#)

mycollection.update_many(
     {'name': 'Iphone 12 Pro Max'},
     {'$set':{
          'name':'Samsung S20 Plus',
          'price': 15500
     }}
)

for i in mycollection.find():
     print(i)

