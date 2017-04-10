#!/usr/bin/env python

"""
This moduled is used by the zabbix_agentd to generate swarm resources
in the LLD Format expected by Zabbix.

For now this modules (and the Docker Python API itself) have support
for nodes and services but not for stacks.
"""

import pdb
import json
import argparse
import docker

CLI = docker.from_env()

class InspectNode():
    """ Stub """

    def __init__(self, args):
        """ Stub """
        self.args = args
        self.cli = docker.from_env()
        self.value = None

    def get_nested_elements(self, info, elements):
        # Function to traverse dictionaries and print when value is 
        # not a dict (instead it's a str)

        if isinstance(elements, str):
            keys = elements.split('.')
        else:
            keys = elements

        for key in keys:
            value = info[key]
            if isinstance(value, dict):
                keys.pop(0)
                if keys:
                    self.get_nested_elements(value, keys)
            elif value is not None:
                #TODO: Verify what is happening to value.
                self.value = value
#                return self.value
            else:
                return('Not Encountered Value')


    def get_node(self):
        """ Return node information """
        node = self.cli.nodes.get(self.args.name)

        attrs = self.args.attrs.split('.')
        self.get_nested_elements(node.attrs, attrs)
        print(self.value)


    def get_service(self):
        """ Return service information """
        # The custom keys will be checked and it they match, the value will
        # be changed to true.
        custom = False
        self.service = self.cli.services.get(self.args.name)

        attrs = self.args.attrs.split('.')

        if self.args.attrs == 'Tasks.Running':
            self.get_working_tasks()
            custom = True

        if self.args.attrs == 'Tasks.Total':
            self.get_total_tasks()
            custom = True

        if not custom:
            self.get_nested_elements(self.service.attrs, attrs)
            print(self.value)

    def get_working_tasks(self,):
        """ Get Running Container/Tasks for the given Service """
        print(len([task for task in self.service.tasks() if 'running' in task['Status']['State']]))

    def get_total_tasks(self):
        """ Return the number of Replicas for the service """
        print(self.service.attrs['Spec']['Mode'].get('Replicated', 'Global').get('Replicas', 1))

# item.attrs["ManagerStatus"]["Reachability"],
#"#NODE_AVAILABLE": item.attrs["Spec"]["Availability"],
#"#NODE_ROLE": item.attrs["Spec"]["Role"],
#"#NODE_STATE": item.attrs["Status"]["State"]
#"#NODE_VERSION": item.attrs["Description"]["Engine"]["EngineVersion"],

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--resource', type=str, choices=['nodes', 'services'], required=True)
    PARSER.add_argument('--name', type=str, required=True)
    PARSER.add_argument('--attrs', type=str, required=True)

    ARGS = PARSER.parse_args()

    resource = InspectNode(args=ARGS)
    if 'nodes' in ARGS.resource:
        resource.get_node()
    if 'services' in ARGS.resource:
        resource.get_service()

