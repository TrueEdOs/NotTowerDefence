import pymongo

from config.settings import Settings


class Database:
    def __init__(self, db_name, col):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client[db_name]
        self.col = db[col]

    def find_login(self, login):
        for item in self.col.find({}, {"_id": 0, "password": 0}):
            if list(item.values())[0] == login:
                return True
        return False

    def load_settings(self):
        for x in self.col.find({}, {"_id": 0}):
            setattr(Settings, list(x.keys())[0], list(x.values())[0])

    def add_settings(self):
        self.col.delete_many({})
        for key in dict(Settings.__dict__):
            if not key.startswith("__"):
                self.col.insert_one({key: Settings.__dict__[key]})

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
#d = Database("Ctalk3r", "settings")
#d.add_settings()
#d.load_settings()
#d.print_db()
