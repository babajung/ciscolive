set IMAGE_NAME=babajung/python3-slim-buster-flask-usecase3a
set CONTAINER_NAME=flask-usecase3a-slim-buster
echo %IMAGE_NAME%
echo %CONTAINER_NAME%

docker build -t %IMAGE_NAME% .

docker run -d -p 8002:5000 --name %CONTAINER_NAME% %IMAGE_NAME%

docker ps -a -f name=%CONTAINER_NAME% --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

docker ps -a -f expose=5000/tcp --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"

netstat -ano | findstr 8002
