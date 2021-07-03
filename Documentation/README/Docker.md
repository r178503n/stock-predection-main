# Docker run and build

docker build -t mytag-production -f Dockerfile.prod .
docker pull ubuntu
docker-compose build
docker-compose up

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
python manage.py runserver 0.0.0.0:8000
docker-compose build
docker-compose up
docker-compose up --build
docker-compose -f docker-compose-prod.yml up
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
cd ClientApp ls

# shut down

docker-compose down

# os

sudo docker save -o vgg_api_image.docker vgg_api

sudo docker load -i vgg_api_image.docker

# ubuntu

sudo docker save -o ubuntu_web_image.docker ubuntu

sudo docker load -i ubuntu_image.docker

# docker web

sudo docker save -o docker_web_image.docker docker_web

sudo docker load -i docker_web_image.docker

# postgress

docker pull postgres
sudo docker save -o postgres_image.docker postgres

# python

sudo docker save -o python3.85_web_image.docker python

sudo docker load -i pythonweb_images.docker

# run

# bash

docker exec -t -i 3bc0574fd4ab /bin/bash

# remove none images

docker rm \$containerID
docker image prune
docker system prune

# ANGULAR

1. Node 15
   docker pull node:14.15.0-alpine3.12

   sudo docker save -o node15.0.1-alpine3.12_web_image.docker node

sudo docker load -i node15.0.1-alpine3.12_web_image.docker

1. Node 14
   sudo docker save -o node15.0.1-alpine3.12_web_image.docker node

sudo docker load -i node15.0.1-alpine3.12_web_image.docker

2. NGINX
   sudo docker save -o nginx1.19.3-alpine_web_image.docker nginx
   sudo docker load -i nginx1.19.3-alpine_web_image.docker
