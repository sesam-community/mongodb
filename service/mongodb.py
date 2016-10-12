import datetime

import bson
import pymongo


class MongoDB(object):

    def __init__(self, host, port, database, username, password):
        self._client = pymongo.MongoClient('mongodb://{host}:{port}'
                                           ''.format(host=host, port=port))
        self._db = self._client[database]
        self._db.authenticate(username, password)

    def insert_or_update(self, collection_name, item):
        collection = self._db[collection_name]
        item['_id'] = item.get('_id', bson.objectid.ObjectId())
        item['_last_modified'] = datetime.datetime.now()
        result = collection.update_one({"_id": item['_id']}, {"$set": item},
                                       upsert=True)
        assert result.acknowledged, 'Insertion failed'
