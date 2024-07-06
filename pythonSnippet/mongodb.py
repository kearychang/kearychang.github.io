import pymongo

client = pymongo.MongoClient("mongodb+srv://k27chang:zer0kakashi@cluster0.kdvow.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.testDb
col = db.col1
post = {"1":2, "3":4, "5":6}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
print(posts.find_one())