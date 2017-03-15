FROM debian:jessie
ADD https://github.com/gcavalcante8808/zbx-docker/releases/download/latest/zbx-docker.tar /usr/local/src/zbx-docker.tar
WORKDIR /usr/local/src
RUN tar xf zbx-docker.tar && \
    chmod +x docker_stats docker_discover

CMD while true; do sleep 1000; done

