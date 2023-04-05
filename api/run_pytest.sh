#!/bin/bash

microservices=("login" "educative_data" "datawebhook" "crud-mongodb" "crud-postgres" "users" "webscraper")

docker-compose up -d

function test_microservice {
  docker-compose exec -T "$1" /bin/bash -c "pytest test_main.py" > testresult.txt || exit 1
  test_result = $(cat testresult.txt)
  if [[ $test_result == *"ERROR"* ]]; then
  echo $test_result
  exit 1
  else
    echo "microservice $1 works!"
  fi
}

for microservice in "${microservices[@]}"
do
  test_microservice "$microservice" 
done


