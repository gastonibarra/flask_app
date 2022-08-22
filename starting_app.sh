#!/bin/bash

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