import pymongo
from bson.objectid import ObjectId 

myclient = pymongo.MongoClient("mongodb+srv://sinemcan1:EaYbRpsdNraof7P8@cluster0.0mfpe.mongodb.net/<dbname>?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort("price")
# Bu durumda fiyat artan şekilde karşımıza gelir.

# Eğer result = mycollection.find().sort("price",-1)
# yaparsak büyükten küçüğe doğru bir sıralama yapılır.

result = mycollection.find().sort("price",-1)

for i in result:
     print(i)


