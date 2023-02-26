from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.xexdmas.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'영수'
    'age':24
}
db.users.insert_one(doc)