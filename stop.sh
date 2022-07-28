sudo docker stop $CONTAINER_NAME

sudo docker rm $(sudo docker ps -aq -f name=$CONTAINER_NAME)
