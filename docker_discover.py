#!/usr/bin/env python
import json
from docker import Client

# A Simple module that returns ids for all docker containers.

cli = Client('http://127.0.0.1:2376')

containers = [ {'{#CONTAINER}': container['Id'], '{#CONTNAME}':  container['Names'][0]} 
               for container in cli.containers(all=True) ]

print(json.dumps({'data': containers}))
