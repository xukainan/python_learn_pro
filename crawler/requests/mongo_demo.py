import pymongo
from bson.objectid import ObjectId


# client = pymongo.MongoClient(host='dev-dsk-shanping-2c-25ba44ef.us-west-2.amazon.com:27017', port=27017)
# client.admin.authenticate("dev", "Aa123456", mechanism='SCRAM-SHA-256')
client = pymongo.MongoClient('mongodb://dev:Aa123456@dev-dsk-shanping-2c-25ba44ef.us-west-2.amazon.com:27017/demo_db')
# client = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format("admin","Aa123456","dev-dsk-shanping-2c-25ba44ef.us-west-2.amazon.com","27017","local"))
db = client["demo_db"]
collection = db.students
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
# 插入
result = collection.insert_one(student)
print(result)

# 查询 它多了 _id 属性，这就是 MongoDB 在插入过程中自动添加的。
result = collection.find_one({'name':'Jordan'})
print(result)

# 根据 ObjectId 来查询
result = collection.find_one({'_id': ObjectId('60b72162fed0728cd6e591f6')})
print(result)

# 年龄大于10的

results = collection.find({'age': {'$gt': 10}})
for result in results:
    print(result)

# 正则
results = collection.find({'name': {'$regex': '^M.*'}})

# 统计
count = collection.find().count()
print(count)

count = collection.find({'age': 20}).count()
print(count)

# 排序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

# 分页
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

# 更新
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)

condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

# 删除
result = collection.remove({'name': 'Kevin'})
print(result)

result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)

#PyMongo 还提供了一些组合方法，如 find_one_and_delete、find_one_and_replace 和 find_one_and_update，它们分别用于查找后删除、替换和更新操作，其使用方法与上述方法基本一致。
#另外，我们还可以对索引进行操作，相关方法有 create_index、create_indexes 和 drop_index 等。