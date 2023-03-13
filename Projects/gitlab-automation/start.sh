#!/bin/bash

git pull

docker compose up --build --remove-orphans --force-recreate -d &
docker compose logs -f test > 2>&1