Docker Zabbix Userparams
------------------------
Simple scripts and userparameter conf to use with zabbix agent and a Docker server or CoreOS (See below).

Introduction
------------

Docker Userparams is a simple set of scripts that supports docker container discovery
and attr introspection.

With this solution, you can start to monitor your docker containers on your Servers.

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

If you want to install this facility into a coreOS image you'll need to use the docker-stats container, because it has all requirements already installed (the container itself have just ~60MB).

Installation - Standard OSes
----------------------------

To install this solution you'll need to do the following steps:

1. Clone the repository into "/usr/share/src/zbx-docker" folder:
    
    git clone https://github.com/gcavalcante8808/zbx-docker.git /usr/share/src/zbx-docker

2. Copy the content of the docker.conf file into the the configuration of your zabbix Agent. If your Zabbix-Agent is configured to include files in a specific Directory, you can copy the file directly to there; 

3. Import Zabbix Template available in the "templates" directory into your Zabbix Environment: 

    * docker17.xml is the template used for Docker 1.7;
    * docker19+.xml is the template used for Docker 1.9 and above;
    * Docker 1.8 MAY be supported by the Docker 1.7 template, but it wasn't tested.
    
4. Link the template against the hosts that have containers running.

Installation - coreOS
---------------------

To install this set scripts on a coreOS system you'll need a zabbix agent installed on it. If you dont have an zabbix agent installed yet, take a look at:

https://github.com/gcavalcante8808/zabbix-agentd-coreos

After the zabbix-agent installation, continue the proccess with the following steps:

1. Create the docker-stats container:

```
docker run -d --name  zabbix-docker-monit -v /var/run/docker.sock:/var/run/docker.sock:ro gcavalcante8808/zbx-docker
```

2. Copy userparameter configuration into your include dir, in the case of zabbix-agentd-coreos it is located at /opt/etc/zabbix/zabbix.agentd.conf.d/:

```
wget https://raw.githubusercontent.com/gcavalcante8808/zbx-docker/master/docker_coreos.conf -O /opt/etc/zabbix/zabbix.agentd.conf.d/docker_coreos.conf
```

3. Restart the zabbix agent:

```
systemctl restart zabbix-agent
```

4. Install the zabbix template located at "templates" in this project into your zabbix server.

Testing the Solution
--------------------

If the target host was configured correctly and the zabbix has received the templates, in a hour new items will
appear in the Host automatically; for now, the templates have support for stats/metrics, discover and the inspect module.

If you want to implement another items, verify the output of the command 'docker inspect <CONTAINER>' to see what can be queried about a 
container.

Other Notes
-----------

 * If you are using the Windows 2016 Server with docker support, you can still use this solution; however, you'll need to install python and 
docker-py package.

 * On Python 3.3 installations, the pip and easy\_install are already present in the setup.
 
 * Python 2.6 is not officially supported ... but you can install requests and argparse libs into it and try to use the solution;

 * You can change the address that will be used to query about containers and discover trough zabbix interface adding a parameter on the discovery or a 3rd parameter in the info, but per default zabbix will not allow unsecure caracters (like @, / and other needed on the URL). In this case, you can create a bash script that wraps the py modules and that passes the --addr parameter with the correct URL of your  API Endpoint.
