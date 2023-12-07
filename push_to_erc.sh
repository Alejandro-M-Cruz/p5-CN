#!/bin/bash

aws ecr get-login-password --region us-east-1 |
  docker login --username AWS --password-stdin 989870301024.dkr.ecr.us-east-1.amazonaws.com

cd "$2"

docker build -t "$1" .
docker tag "$1:latest" "989870301024.dkr.ecr.us-east-1.amazonaws.com/$1:latest"
docker push "989870301024.dkr.ecr.us-east-1.amazonaws.com/$1:latest"
