$env:IMAGE_NAME="babajung/python3-slim-buster-flask-usecase3a"
$env:CONTAINER_NAME="flask-usecase3a-slim-buster"

echo $env:IMAGE_NAME
echo $env:CONTAINER_NAME

docker build -t $env:IMAGE_NAME .

docker run -d -p 8002:5000 --name $env:CONTAINER_NAME $env:IMAGE_NAME

docker ps -a -f name=$env:CONTAINER_NAME --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

docker ps -a -f expose=5000/tcp --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

netstat -ano | findstr 8002
