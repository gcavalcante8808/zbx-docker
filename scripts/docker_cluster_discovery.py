#!/usr/bin/env python

import json
import argparse
import docker

class SwarmInspect:
    def __init__(self, func=None):
        cli = docker.from_env()

        if func:
            self.execute = func(cli)

    def execute(self):
        print("No EndPoint Resource Provided")


def discovery_nodes(cli):
    node_list = cli.nodes.list()

    nodes = [{
               "{#NODE_NAME}": item.attrs["Description"]["Hostname"],
               "{#NODE_ID}": item.id,
             }
              for item in node_list]

    print(json.dumps({'data': nodes}))


def extrode_multiple_urls(urls):
    """ Return the last (right) url value """
    if urls and len(urls) > 1:
        return urls[-1]
    
    return urls

def discovery_services(cli):
    services_list = cli.services.list()

    services = [{
                 "{#SERVICE_ID}": item.id,
                 "{#SERVICE_NAME}": item.name,
                 "{#SERVICE_HTTPSUPPORT}": 
                      extrode_multiple_urls(item.attrs['Spec']['Labels'].get('com.df.serviceDomain', False))
              } for item in services_list]

    print(json.dumps({'data': services}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--resource', type=str, choices=['nodes','services'], required=True)
    
    args = parser.parse_args()
    
    
    if 'nodes' in args.resource:
        sinspect = SwarmInspect(discovery_nodes)
    else:
        sinspect = SwarmInspect(discovery_services)

