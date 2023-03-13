#!/bin/bash

git reset --hard origin && git pull && chmod u+x -R *

git pull

docker compose up --build --remove-orphans --force-recreate

###############################
## Testing Output
###############################
docker compose logs -f test > 2>&1
