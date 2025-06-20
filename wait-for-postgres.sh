#!/bin/sh
# wait-for-postgres.sh

until pg_isready -h db -p 5432 -U $POSTGRES_USER; do
  echo "Waiting for postgres..."
  sleep 1
done

exec "$@"