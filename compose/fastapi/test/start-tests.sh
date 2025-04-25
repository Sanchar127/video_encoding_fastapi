#!/bin/bash

# Wait for the database and other dependencies to be ready
echo "Waiting for MySQL..."
until nc -z -v -w30 mysqldb 3306
do
  echo "Waiting for MySQL to be ready..."
  sleep 5
done

# Optionally, wait for other services like RabbitMQ or Dragonfly here in a similar way

# Run the tests
echo "Running tests..."
pytest --maxfail=1 --disable-warnings -q
