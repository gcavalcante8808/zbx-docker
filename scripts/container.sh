#!/bin/sh

if [ ! -f /var/run/docker.sock ]; then
    echo "You should provide docker.sock as a ro volume to use this container"
    exit 1
fi

while true; do echo Stub CMD; sleep 100; done
