#mongodb-datasink

A python micro service for receiving a JSON entity stream from a Sesam service
instance and pushing them to MongoDB.

[![Build Status](https://travis-ci.org/sesam-community/mongodb-sink.svg?branch=master)](https://travis-ci.org/sesam-community/mongodb-sink)

A docker image is provided here: <https://hub.docker.com/r/giskou/mongodb-sink/>

    docker run -it --rm \
      --name=mongodb-sink \
      --network=<network> \
      -p 5001:5001 \
      -e MONGODB_HOST=<host> \
      -e MONGODB_PORT=<port> \
      -e MONGODB_USERNAME=<username> \
      -e MONGODB_PASSWORD=<password> \
      -e MONGODB_DATABASE=<database> \
      giskou/mongodb-sink

* **MONGODB\_HOST**: the hostname of the mongodb instance the sink will connect
  to. _(default: localhost)_
* **MONGODB\_PORT**: the port of the mongodb instance the sink will connect to.
  _(default: 27017)_
* **MONGODB\_DATABASE**: the database to push data to
* **MONGODB\_USERNAME**: the username of database user
* **MONGODB\_PASSWORD**: the password of the database user

The service is running on port 5001 and accepts connections to the following
endpoint:

    POST /<collection>

`collection` is the collection to push the data into.
If it does not exist it will be created.
