from pymongo import MongoClient


class Memory:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db['memory']

    def save_interaction(self, input, output):
        self.collection.insert_one({"input": input, "output": output})

    def get_data(self, context):
        # Adjust this method according to how you want to retrieve memory data
        return self.collection.find_one(context)
