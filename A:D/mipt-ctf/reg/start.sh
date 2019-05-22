#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

export HOST_IP=$(/sbin/ip route | awk '/enp0s3/ { print $9 }' | sed -n 2p)

docker-compose up --build -d
