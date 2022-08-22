# Flask API

## Description

Small Flask app for educational purposes. It's a API server writed with Python
and a MongoDB as the backend.

In the other hand, we have CI/CD with a local Jenkins that will deploy the new changes
in the Container from Docker Hub to a Kubernetes's Cluster.

## Configuration

The API server is configured through environment variables.

| Environment Variable | Default Value             |
| -------------------- | ------------------------- |
| MONGO_URI            | mongodb://127.0.0.1:27017 |
| MONGO_DB             | restdb                    |

## Installation

### Dependencies

- python3
- mongodb
- python3-pip
- virtualenv

### Deployment with Bash and virtualenv

```bash
echo "Installing Mongo DB"
mkdir -p mongo/data/db
apt-get update
apt-get install -y mongodb
mongod --fork --logpath /var/log/mongodb/mongod.log --dbpath mongo/data/db --noauth


echo "Mongo DB installed"
echo " Starting App"

virtualenv -p python3.8 venv/py38
source venv/py38/bin/activate
/usr/bin/pip install -r requirements.txt
cd api
/usr/bin/python3.8 -m flask run --host=0.0.0.0 --port "5000"
```

## Tests

### POST method to save a new product in our database.

```bash

curl --location --request POST 'http://127.0.0.1:5000/api/new' \
--header 'Content-Type: application/json' \
--data-raw {"name" : "Notebook", "price": 1000, "id" : 63}
```

### GET method to retrieve products in our database.

```bash

curl --location --request GET 'http://127.0.0.1:5000/api/products' \
--header 'Content-Type: application/json' \
--data-raw {"id" : 63}
```

### DELETE method to retrieve products in our database.

```bash

curl --location --request DELETE 'http://127.0.0.1:5000/api/products' \
--header 'Content-Type: application/json' \
--data-raw {"id" : 63}

```

#text to test the pipeline.
