#!/usr/bin/env python
import json
from docker import Client

# A Simple module that returns ids for all docker containers.

cli = Client('unix://var/run/docker.sock')

containers = [ {'#CONTAINER': container['Id']} 
               for container in cli.containers(all=True) ]

print(json.dumps(containers))
