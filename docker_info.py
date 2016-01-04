#!/usr/bin/env python
import json
import argparse
from docker import Client

# A Simple module that returns attributes values for given ids.
def get_container_attr(container_id, attr):
    # Find a container info and return desired attr.
    cli = Client('unix://var/run/docker.sock')
    container = cli.inspect_container(container_id)
    print(json.dumps(container[attr]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cid', type=str, required=True)
    parser.add_argument('--attr', type=str, required=True)

    args = parser.parse_args()
    
    get_container_attr(container_id=args.cid, attr=args.attr)

