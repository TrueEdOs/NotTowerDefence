import pymongo


class Database:
    def __init__(self, col):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["database"]
        self.col = db[col]

    def find_login(self, login):
        for item in self.col.find({}, {"_id": 0, "password": 0}):
            if list(item.values())[0] == login:
                return True
        return False

    def find_user(self, login, password):
        if self.col.find_one({"login": login, "password": password}):
            return True
        return False

    def print_db(self):
        for x in self.col.find({}, {"_id": 0}):
            print(x)

    def add_user(self, login, password):
        if not self.find_login(login):
            self.col.insert_one({"login": login, "password": password})

    def clear_db(self):
        self.col.delete_many({})
        self.col.drop()

#d = Database("user_data")
#d.print_db()
