FROM python:3.8-alpine
LABEL Auther="jon4hz"
WORKDIR /usr/src/app
RUN apk add gcc musl-dev libffi-dev openssl-dev python3-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY watcher.py ./
RUN mkdir ./data/
VOLUME ./data
CMD ["python", "./watcher.py"]