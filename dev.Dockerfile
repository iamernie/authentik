FROM beryju/passbook-base:latest

RUN pip install -r /app/requirements-dev.txt  --no-cache-dir
