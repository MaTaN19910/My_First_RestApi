#!/bin/bash
input="/home/maoolin/flaskapp/docker.txt"
while IFS= read -r line
do
 sudo docker rmi $line
done < "$input"
