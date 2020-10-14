import pymongo

m = {
    "이름":"안준석",
    "나이":29,
    "프로필":[
        "a.jpg",
        "b.jpg"
    ]    
}

m2 = {
    "이름":"안준석",
    "나이":29,
    "지역": "대구",
    "프로필":[
        "a.jpg",
        "b.jpg"
    ]    
}

conn = pymongo.MongoClient("localhost", 27017)
db = conn.test
col = db.members

col.insert_one(m2)

results = col.find()
for r in results:
    print(r)

# 이름이 안준석 and 지역이 서울
results2 = col.find({"이름" : "안준석", "지역":"서울"})
for r in results2:
    print(r)

results3 = col.find({"$or": [{"이름":"안준석"}, {"나이":30} ]})
for r in results3:
    print(r)
    
col.update_one(
    {"이름":"안준석"},
    {"$set":
        {"이름":"Junseok Ahn"}
    }
)

col.update_many(
    {"이름":"안준석"},
    {"$set":
        {"이름":"Junsoku Ahn"}
    }
)

col.delete_many(
    {"이름":"Junseok Ahn"}
)