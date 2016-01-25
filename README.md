Docker Zabbix Userparams
------------------------
Simple scripts and userparameter conf to use with zabbix agent and a Docker server.

Introduction
------------

Docker Userparams is a simple set of scripts that supports docker container discovery
and attr introspection.

With this solution, you can start to monitor your docker containers on your Zabbix Server.

Requirements
------------

For now, the docker server should have an HTTP API point available on the host (the scripts uses the http://127.0.0.1:2376 as default api address).

Python 2.7+ (Including Python 3+) is required, and the Docker-Py is required as well.

If you don't have the docker-py installed, you can install it trough the following command (requires PIP, will install a system-wide version):

```
# pip install docker-py

```

If you need help to configure your docker server to have an API point, you can follow the instruction available on the docker page:

 * https://docs.docker.com/engine/reference/api/docker\_remote\_api/

Installation
------------

To install this solution you'll need to do the following steps:

1. Clone the repository into a folder (usually with git clone command);
2. Copy 'docker.conf' into your zabbix agent configuration directory (/etc/zabbix/zabbix.conf.d/ if using official packages from zabbix sia)
3. Copy 'docker\_discover.py' to /data (Or change the path on the docker.conf file);
4. Copy 'docker\_inf.py' to /data';
5. Import Zabbix Template available in the directory into your Zabbix Environment;
6. Link the template against the hosts that have containers running.

Testing the Solution
--------------------

If the target host was configured correctly and the zabbix has received the templates, in some minutes (10 per default) new hosts will
appear in the 'Docker Container' Group automatically; for now, the templates just monitor the 'State' of the containers.

If you want to implement another items, verify the output of the command 'docker inspect <CONTAINER>' to see what can be queried about a 
container.

Other Notes
-----------

 * If you are using the Windows 2016 Server with docker support, you can still use this solution; however, you'll need to install python and 
docker-py package.

 * On Python 3.3 installations, the pip and easy\_install are already present in the setup.

 * For Now, Its not Possible to get nested items, like 'State.Running'.

 * You can change the address that will be used to query about containers and discover trough zabbix interface adding a parameter on the discovery or a 3rd parameter in the info, but per default zabbix will not allow unsecure caracters (like @, / and other needed on the URL). In this case, you can create a bash script that wraps the py modules and that passes the --addr parameter with the correct URL of your  API Endpoint.
