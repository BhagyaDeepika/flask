

WORKDIR /app

COPY . /app
RUN apk add build-base
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
   
RUN pip3 install -r requirements.txt

EXPOSE 4800

ENTRYPOINT  ["python"]

CMD ["app.py"]
