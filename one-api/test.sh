#!/bin/bash

printf '\n\nTesting get all user info...\n\n'
curl -i http://localhost:5000/one/api/v1.0/

printf '\n\nTesting get single user...\n\n'
curl -i http://localhost:5000/one/api/v1.0/points/2

printf '\n\nTesting get invalid user...\n\n'
curl -i http://localhost:5000/one/api/v1.0/points/3

printf '\n\nTesting insert and get new user...\n\n'
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"John"}' http://localhost:5000/one/api/v1.0/points
curl -i http://localhost:5000/one/api/v1.0/points/3

printf '\n\nTesting add points and get user...\n\n'
curl -i http://localhost:5000/one/api/v1.0/
curl -i -H "Content-Type: application/json" -X PUT -d '{"points":1}' http://localhost:5000/one/api/v1.0/points/3
curl -i http://localhost:5000/one/api/v1.0/

printf '\n\nTesting remove currency and get user...\n\n'
curl -i http://localhost:5000/one/api/v1.0/
curl -i -H "Content-Type: application/json" -X PUT -d '{"currency":1}' http://localhost:5000/one/api/v1.0/currency/3
curl -i http://localhost:5000/one/api/v1.0/

printf '\n\nTesting remove added user\n\n'
curl -i http://localhost:5000/one/api/v1.0/
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/one/api/v1.0/points/3
curl -i http://localhost:5000/one/api/v1.0/
