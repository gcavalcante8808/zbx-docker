Docker Zabbix Userparams
------------------------
Simple scripts and userparameter conf to use with zabbix agent and a Docker server. 

Introduction
------------

Docker Userparams is a simple set of scripts that supports docker container discovery
and attr introspection.

With this solution, you can start to monitor your docker containers on your Servers.

Requirements
------------

For now, the Zabbix User should have access to the docker socket.


Installation - Standard 
-----------------------

To install this solution you'll need to do the following steps:

1. Download the latest version of the binaries into the "/usr/local/src" folder using the command (or similar):

```
wget https://github.com/gcavalcante8808/zbx-docker/releases/download/latest/zbx-docker.tar -O /usr/local/src/zbx-docker.tar 
```

2. Descompact the file and make each file executable:

```
cd /usr/local/src/
tar xf /usr/local/src/zbx-docker.tar
chmod +x /usr/local/src/zbx-docker.tar
```

3. Install the UserParameters available at https://raw.githubusercontent.com/gcavalcante8808/zbx-docker/master/docker_bare.conf.

4. Install the templates available at https://github.com/gcavalcante8808/zbx-docker/tree/master/templates and link the docker server templates.

After some minutes (10 by default) new hosts will be created at the Docker Containers Group.


Installation - Container
------------------------

Instead of losing time copying and configuring things, you can use a container instead. To use the container run the following commands

```
docker run -d -v /var/run/docker.sock:/var/run/docker.sock:ro gcavalcante8808/zbx-docker
```

After this command, install the userparameters available at https://raw.githubusercontent.com/gcavalcante8808/zbx-docker/master/docker.conf and the templates.

Other Notes
-----------

 * If you are using the Windows 2016 Server with docker support, you can still use this solution; however, you'll need to install python and 
docker-py package and use the scripts instead..

 * You can change the address that will be used to query about containers and discover trough zabbix interface adding a parameter on the discovery or a 3rd parameter in the info, but per default zabbix will not allow unsecure caracters (like @, / and other needed on the URL). In this case, you can create a bash script that wraps the py modules and that passes the --addr parameter with the correct URL of your  API Endpoint.
