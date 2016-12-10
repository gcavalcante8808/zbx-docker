#!/usr/bin/env python
import json
import argparse
import docker

# A Simple module that returns stats for given ids.


def get_nested_elements(info, elements):
    # Function to traverse dictionaries and print when value is 
    # not a dict (instead it's a str)
#    pdb.set_trace()

    if isinstance(elements, str):
        keys = elements.split('.')
    else:
        keys = elements

    for key in keys:
        value = info[key]
        if isinstance(value, dict):
            keys.pop(0)
            if keys:
                get_nested_elements(value, keys)
        elif value is not None:
            print(value)
        else:
            return('Not Encountered Value')

def get_container_attr(container_id, attr, addr):
    # Find a container info and return desired attr.
    cli = docker.from_env()
    container = cli.stats(container_id, stream=False)
    get_nested_elements(container, attr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cid', type=str, required=True)
    parser.add_argument('--attr', type=str, required=True)
    parser.add_argument('--addr', type=str, required=False)

    args = parser.parse_args()

    if not args.addr:
        addr = 'http://127.0.0.1:2376'
    
    get_container_attr(container_id=args.cid, attr=args.attr, addr=addr)

