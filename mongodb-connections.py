import pymongo

myclient = pymongo.MongoClient("mongodb+srv://sinemcan1:EaYbRpsdNraof7P8@cluster0.0mfpe.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]

mycollection = mydb["products"]

print(mydb.list_collection_names())