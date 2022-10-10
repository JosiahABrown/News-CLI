#!/bin/sh
# Run the file

docker run -d -p 4444:4444 --shm-size=2g --name standalone-chrome selenium/standalone-chrome:3.141.59-20210929
python3 main.py 
docker stop standalone-chrome 
docker rm standalone-chrome
