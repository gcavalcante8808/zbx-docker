#!/usr/bin/env python
import json
import argparse
import docker

# A Simple module that returns ids for all docker containers.
def print_discover(addr):
    cli = docker.from_env()

    containers = [{'{#CONTAINER}':container.id, '{#CONTNAME}': container.name,
                   '{#IMAGE}': container.attrs['Config']['Image'], '{#LOGPATH}': container.attrs['LogPath'],
                   '{#STATE}': container.status}
               for container in cli.containers.list(all=True)]

    print(json.dumps({'data': containers}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--addr', type=str, required=False)

    args = parser.parse_args()

    if not args.addr:
        addr = 'http://127.0.0.1:2376'
    
    print_discover(addr=addr)

