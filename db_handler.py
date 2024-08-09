from pymongo import MongoClient

class DatabaseHandler:
    def __init__(self, connection_string='mongodb://localhost:27017/'):
        try:
            self.client = MongoClient(connection_string)
            self.db = self.client['mqtt_database']
            self.collection = self.db['messages']
        except Exception as e:
            raise e

    def insert_message(self, message):
        try:
            self.collection.insert_one(message)
        except Exception as e:
            raise e

    def get_status_counts(self, start_time, end_time):
        try:
            pipeline = [
                {
                    '$match': {
                        'timestamp': {'$gte': start_time, '$lte': end_time}
                    }
                },
                {
                    '$group': {
                        '_id': '$status',
                        'count': {'$sum': 1}
                    }
                }
            ]
            
            result = list(self.collection.aggregate(pipeline))
            return {item['_id']: item['count'] for item in result}
        except Exception as e:
            raise e