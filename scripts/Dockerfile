FROM python:3.5-onbuild
RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils \
    upx-ucl && \
    apt-get clean && \
    rm -rf /var/lib/apt/*

RUN pyinstaller -F docker_discover.py && \
    pyinstaller -F docker_stats.py

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"

