#!/usr/bin/env python
import json
import argparse
from docker import Client

# A Simple module that returns attributes values for given ids.
def get_container_attr(container_id, attr, addr):
    # Find a container info and return desired attr.
    cli = Client(addr)
    container = cli.inspect_container(container_id)
    print(json.dumps(container[attr]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cid', type=str, required=True)
    parser.add_argument('--attr', type=str, required=True)
    parser.add_argument('--addr', type=str, required=False)

    args = parser.parse_args()

    if not args.addr:
        addr = 'http://127.0.0.1:2376'
    
    get_container_attr(container_id=args.cid, attr=args.attr, addr=addr)

