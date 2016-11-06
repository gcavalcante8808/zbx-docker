#!/usr/bin/env python
import json
import argparse
from docker import Client

# A Simple module that returns ids for all docker containers.
def print_discover(addr):
    cli = Client(base_url=addr, version='auto')

    containers = [ {'{#CONTAINER}': container['Id'], '{#CONTNAME}':  container['Names'][-1:][0].strip('/'), '{#IMAGE}': container['Image'] } 
               for container in cli.containers(all=True) ]

    print(json.dumps({'data': containers}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--addr', type=str, required=False)

    args = parser.parse_args()

    if not args.addr:
        addr = 'http://127.0.0.1:2376'
    
    print_discover(addr=addr)

