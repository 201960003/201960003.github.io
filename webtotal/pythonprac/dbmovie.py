from pymongo import MongoClient
import certifi 

ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.xexdmas.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# 실수로 title을 tltle로 저장했음
movie = db.movies.find_one({'tltle':'가버나움'})
target_star = movie['star']

db.movies.update_one({'tltle':'가버나움'},{'$set':{'star':'0'}})

movies = list(db.movies.find({'star':target_star}))
print(movies)
for a in movies:
    print(a['tltle'])

