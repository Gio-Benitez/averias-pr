msg1='$'
ms=":"
msg2="$ms Building docker image..."
echo "$msg2"
#docker build -t averiaspr_database .
#sleep 1
#msg2="$ms Docker image has been built."
#echo "$msg2"

#msg2="$ms Removing any duplicate containers if necessary"
#echo "$msg2"
#docker kill averiaspr_database
#sleep 1

#docker rm averiaspr_database
#sleep 1

#msg2="$ms Creating container"
#echo "$msg2"
#docker run --name averiaspr_database -e POSTGRES_USER=root -e POSTGRES_PASSWORD=password -e POSTGRES_DB=AVERIASPR_DATABASE -p 5432:5432 -d postgres

docker-compose up