$env:CONTAINER_ID=$(docker ps -aq -f name=$env:CONTAINER_NAME)
echo $env:CONTAINER_ID

$env:IMAGE_ID=$(docker image ls $env:IMAGE_NAME --format "{{.ID}}")
echo $env:IMAGE_ID

docker stop $env:CONTAINER_NAME
docker rm $env:CONTAINER_ID

docker image rm $env:IMAGE_ID
