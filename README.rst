================
mongodb-datasink
================

A python micro service for receiving a JSON entity stream from a Sesam service
instance and pushing them to MongoDB.

A docker image is provided here: <https://hub.docker.com/r/giskou/mongodb-sink/>

    docker run -it --rm \
      --name=mongodb-sink \
      --network=<network> \
      -p 5001:5001 \
      -e MONGODB_HOST=<host> \
      -e MONGODB_USERNAME=<username> \
      -e MONGODB_PASSWORD=<password> \
      -e MONGODB_DATABASE=<northwind> \
      giskou/mongodb-sink:dev

_MONGODB_HOST_: the hostname of the mongodb instace the sink will connect to.
(default: localhost)

_MONGODB_PORT_: the port of the mongodb instace the sink will connect to.
(default: 27017)

_MONGODB_DATABASE_: the database to push data to

_MONGODB_USERNAME_: the username of database user

_MONGODB_PASSWORD_: the password of the database user
