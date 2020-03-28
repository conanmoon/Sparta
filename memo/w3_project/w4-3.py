from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

avengers = db.movies.find_one({'title': '어벤져스: 엔드게임'}, {'_id': 0})
print(avengers)

target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})
target_star = target_movie['star']

# movies = list(db.movies.find({'star': target_star})) #list because of find multiples

# for i in movies:
#     db.movies.update_one({'star': target_star}, {'$set': {'star': 0}})
#     print(i)

# 생김새
db.movies.update_many({'star': target_star}, {'$set': {'star': 0}})
