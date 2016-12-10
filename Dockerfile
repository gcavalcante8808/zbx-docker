FROM alpine
RUN apk add --update python curl && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install docker-py
COPY scripts/* /usr/local/src/
CMD while true; do echo Stub CMD; sleep 100; done
