# Cisco Live Search

## Git clone

```
git clone https://github.com/babajung/ciscolive.git
```

## DOCKER BUILD AND RUN

**Windows (cmd)**
```
set IMAGE_NAME=babajung/python3-slim-buster-flask-usecase3a
set CONTAINER_NAME=flask-usecase3a-slim-buster
echo %IMAGE_NAME%
echo %CONTAINER_NAME%

docker build -t %IMAGE_NAME% .

#docker run --rm -p 8002:5000 --name %CONTAINER_NAME% %IMAGE_NAME%

# run as daemon
docker run -d -p 8002:5000 --name %CONTAINER_NAME% %IMAGE_NAME%

docker ps -a -f name=%CONTAINER_NAME% --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

docker ps -a -f expose=5000/tcp --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

netstat -ano | findstr 8002
```

**Powershell**
```
$env:IMAGE_NAME="babajung/python3-slim-buster-flask-usecase3a"
$env:CONTAINER_NAME="flask-usecase3a-slim-buster"

echo $env:IMAGE_NAME
echo $env:CONTAINER_NAME

docker build -t $env:IMAGE_NAME .

#docker run --rm -p 8002:5000 --name $env:CONTAINER_NAME $env:IMAGE_NAME

# run as daemon
docker run -d -p 8002:5000 --name $env:CONTAINER_NAME $env:IMAGE_NAME

docker ps -a -f name=$env:CONTAINER_NAME --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

docker ps -a -f expose=5000/tcp --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

netstat -ano | findstr 8002
```

**Linux**
```
export IMAGE_NAME=babajung/python3-slim-buster-flask-usecase3a
export CONTAINER_NAME=flask-usecase3a-slim-buster
echo $IMAGE_NAME
echo $CONTAINER_NAME

sudo docker build -t $IMAGE_NAME .

#sudo docker run --rm -p 8002:5000 --name $CONTAINER_NAME $IMAGE_NAME

# run as daemon
sudo docker run -d -p 8002:5000 --name $CONTAINER_NAME $IMAGE_NAME

sudo docker ps -a -f name=$CONTAINER_NAME --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

sudo docker ps -a -f expose=5000/tcp --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

sudo netstat -anulpt | grep :8002

```

## DOCKER STOP RUNNING

**Windows (cmd)**
```
docker stop %CONTAINER_NAME%
```

**Powershell**
```
$env:CONTAINER_ID=$(docker ps -aq -f name=$env:CONTAINER_NAME)
echo $env:CONTAINER_ID

$env:IMAGE_ID=$(docker image ls $env:IMAGE_NAME --format "{{.ID}}")
echo $env:IMAGE_ID

docker stop $env:CONTAINER_NAME
docker rm $env:CONTAINER_ID

docker image rm $env:IMAGE_ID
```

**Linux**
```
sudo docker stop $CONTAINER_NAME

sudo docker rm $(sudo docker ps -aq -f name=$CONTAINER_NAME)
```

## DOCKER TROUBLESHOOTING

**Windows (cmd)**
```
docker exec -it %CONTAINER_NAME% /bin/sh
```

**Powershell**
```
docker exec -it $env:CONTAINER_NAME /bin/sh
```

**Linux**
```
docker exec -it $IMAGCONTAINER_NAMEE_NAME /bin/sh
```
