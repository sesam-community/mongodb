import datetime

import bson
import pymongo
import pymongo.operations


class MongoDB(object):

    def __init__(self, host, port, database, username, password):
        self._client = pymongo.MongoClient('mongodb://{host}:{port}'
                                           ''.format(host=host, port=port))
        self._db = self._client[database]
        self._db.authenticate(username, password)

    def create_or_update(self, collection_name, items):
        collection = self._db[collection_name]
        operations = []
        for item in items:
            item['_id'] = item.get('_id', bson.objectid.ObjectId())
            item['_last_modified'] = datetime.datetime.now()
            operation = pymongo.operations.ReplaceOne({"_id": item['_id']},
                                                      item, upsert=True)
            operations.append(operation)

        result = collection.bulk_write([operations])
        assert result.acknowledged, 'Insertion failed'
