pip install -r requirements.txt
rm -rf postgres-data
docker-compose down --rmi all --volumes
docker-compose up --force-recreate