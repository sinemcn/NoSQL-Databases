import pymongo
from bson.objectid import ObjectId 

myclient = pymongo.MongoClient("mongodb+srv://sinemcan1:EaYbRpsdNraof7P8@cluster0.0mfpe.mongodb.net/<dbname>?retryWrites=true&w=majority")

mydb = myclient["node-app"]

mycollection = mydb["products"]

# Eğer tekli kayıt yapacaksak find_one() kullanırız.
# result = mycollection.find_one()
# print(result)

# Eğer çoklu kayıt yapacaksak find() kullanırız.Bu çoklu kayıtları for döngüsü kullanarak yazdırabiliriz.
# for i in mycollection.find():
     # print(i)

# Eğer istediğimiz değeri yazdırmak istersek quary metodunu atarız ve böylelikle istediğimiz değerleri "1" ya da "0"
# değerlerini atayarak yazdırıp yazdırmamaya karar veririz.

for i in mycollection.find({},{"name":0}):
     print(i)

