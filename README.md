Docker Zabbix Userparams
------------------------
Simple scripts and userparameters conf to use with zabbix agent and a Docker server.

Introduction
------------

Docker Userparams is a simple set of scripts that supports docker container discovery
and attr introspection.

With this solution, you can start to monitor your docker containers on your Zabbix Server.

Requirements
------------

For now, the zabbix user should have read permission on '/var/run/docker.sock'; in the future the modules aims to provide
to support docker tcp enabled setups.

Python 2.7+ (Including Python 3+) is required.

Docker-Py is another requirement.

If you don't have the docker-py installed, you can install it trough the following command (requires PIP, will install a system-wide version):

```
# pip install docker-py

```

Installation
------------

To install this solution you'll need to do the following steps:

1. Clone the repository into a folder (usually with git clone command);
2. Copy 'docker.conf' into your zabbix agent configuration directory (/etc/zabbix/zabbix.conf.d/ if using official packages from zabbix sia)
3. Copy 'docker\_discover.py' to /tmp;
4. Copy 'docker\_inf.py' to /tmp';
5. Import Zabbix Template into your Zabbix Environment;
6. Link the template against the needed hosts.

Other Notes
-----------

If you are using the Windows 2016 Server with docker support, you can still use this solution; however, you'll need to install python and 
docker-py package.

On Python 3.3 installations, the pip and easy\_install are already present in the setup.

