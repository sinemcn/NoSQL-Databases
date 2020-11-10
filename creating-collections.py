import pymongo

myclient = pymongo.MongoClient("mongodb+srv://sinemcan1:EaYbRpsdNraof7P8@cluster0.0mfpe.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]

mycollection = mydb["products"]
"""
products = {"name":"Iphone 11","price":15000}

result = mycollection.insert_one(products)

print(result)
print(type(result))
print(result.inserted_id)
"""

# BİRDEN FAZLA KAYDI COLLECTIONS OLARAK EKLEMEK İSTERSEK ;

products_list = [
     {"name":"Iphone 7","price":7000, "description": "iyi telefon"},
     {"name":"Iphone 8","price":8000, "categories": ['telefon','elektronik']},
     {"name":"Iphone 10","price":9000},
     {"name":"Iphone 11","price":10000},
     {"name":"Iphone 11 Pro Max","price":11000},
     {"name":"Iphone 12","price":12000},
     {"name":"Iphone 12 Pro","price":13000},
     {"name":"Iphone 12 Pro Max","price":14000}
]

result = mycollection.insert_many(products_list)
print(result.inserted_ids)