#!/usr/bin/env python
import json
import argparse
import docker

# A Simple module that returns attributes values for given ids.


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
        elif value:
            print(value)
        else:
            return('Value Not found')

def get_container_attr(container_id, attr):
    # Find a container info and return desired attr.
    cli = docker.from_env()
    container = cli.containers.get(container_id)
    get_nested_elements(container.attrs, attr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cid', type=str, required=True)
    parser.add_argument('--attr', type=str, required=True)

    args = parser.parse_args()
    
    get_container_attr(container_id=args.cid, attr=args.attr)
