export IMAGE_NAME=babajung/python3-slim-buster-flask-usecase3a
export CONTAINER_NAME=flask-usecase3a-slim-buster
echo $IMAGE_NAME
echo $CONTAINER_NAME

sudo docker stop $CONTAINER_NAME
sudo docker rm $(sudo docker ps -aq -f name=$CONTAINER_NAME)

sudo docker build -t $IMAGE_NAME .
sudo docker run -d -p 8002:5000 --name $CONTAINER_NAME $IMAGE_NAME

sudo docker ps -a -f name=$CONTAINER_NAME --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

sudo docker ps -a -f expose=5000/tcp --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

sudo netstat -anulpt | grep :8002

#sudo docker stop $CONTAINER_NAME

#sudo docker rm $(sudo docker ps -aq -f name=$CONTAINER_NAME)