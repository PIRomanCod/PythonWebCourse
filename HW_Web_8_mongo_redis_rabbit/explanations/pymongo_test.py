from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://4751413:sEe4atcemRuzYfBj@cluster0.ixwjqpd.mongodb.net/?retryWrites=true&w=majority")

db = client.book
#
# result_one = db.cats.insert_one(
#     {
#         "name": "barsik",
#         "age": 3,
#         "features": ["ходить в капці", "дає себе гладити", "рудий"],
#     }
# )
#
# print(result_one.inserted_id)
#
# result_many = db.cats.insert_many(
#     [
#         {
#             "name": "Lama",
#             "age": 2,
#             "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
#         },
#         {
#             "name": "Liza",
#             "age": 4,
#             "features": ["ходить в лоток", "дає себе гладити", "білий"],
#         },
#     ]
# )
# print(result_many.inserted_ids)
#
# result = db.cats.find_one({"_id": ObjectId("6401ce676ac1880c926e2049")})
# print(result)

result = db.cats.find({})
for el in result:
    print(el)

# db.cats.delete_one({"name": "barsik"})
# result = db.cats.find_one({"name": "barsik"})
# print(result)