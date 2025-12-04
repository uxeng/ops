#!/usr/bin/env bash
export BUILD_ENV="local"
docker container stop uxeng
docker container rm uxeng
docker system prune -a -f
docker image rm  "uxeng:Dockerfile"
docker build -t "uxeng:Dockerfile" .
docker run --name uxeng --publish 3000:3000 "uxeng:Dockerfile"
