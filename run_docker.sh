#!/usr/bin/env bash
echo removing old containers
docker stop $(docker ps -a -q)

echo building docker containers
docker-compose up --build -d

echo Dash App status
if [ $(curl -LI http://127.0.0.1:8000 -o /dev/null -w '%{http_code}\n' -s) == "200" ]; then echo Dash app running; fi
