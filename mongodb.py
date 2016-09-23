from pymongo import MongoClient
client = MongoClient()
db = client.test_database
collection = db.test_collection

import datetime
post = {"author":"Mike", "test":"testing",
	"tags":["mongo","python","tired"],
	"date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

print posts.find_one()
print posts.count()
