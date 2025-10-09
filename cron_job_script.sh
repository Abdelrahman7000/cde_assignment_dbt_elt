#!/bin/bash

# Define the directory where docker-compose.yml is located
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $PROJECT_DIR

echo "Starting Postgres service..."
# Start the postgres_db 
docker compose up -d postgres_db

sleep 20

echo "Extract the data and Load it into postgres via python ...."
# Use `docker compose run` to execute the python_etl container once
# --no-deps ensures only this service is (re)created and run
docker compose run --rm python_etl

if [ $? -ne 0 ]; then
    echo "Python E&L failed. Aborting pipeline."
    exit 1
fi

echo "Transforming the loaded data via dbt."
# Use `docker compose run` to execute dbt commands
# `dbt run` executes all models
docker compose run --rm dbt_transform dbt run

if [ $? -ne 0 ]; then
    echo "dbt run failed."
fi


echo "Pipeline finished successfully."