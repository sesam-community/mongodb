import json
import os

import flask
import mongodb

app = flask.Flask(__name__)

mongodb_host = os.getenv('MONGODB_HOST', 'localhost')
mongodb_port = os.getenv('MONGODB_PORT', '27017')

mongodb_database = os.getenv('MONGODB_DATABASE')
mongodb_username = os.getenv('MONGODB_USERNAME')
mongodb_password = os.getenv('MONGODB_PASSWORD')

mdb = mongodb.MongoDB(mongodb_host, mongodb_port, mongodb_database,
                      mongodb_username, mongodb_password)

@app.route('/<collection>', methods=['POST'])
def receiver(collection):
    mdb.create_or_update(collection, flask.request.get_json())
    return flask.Response("Thanks!", mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
