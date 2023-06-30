FROM alpine:latest

#RUN apk add --no-cache python3-dev && pip3 install --upgrade pip
RUN apk add --no-cache python3

WORKDIR /app
COPY . /app
RUN python3 /app/get-pip.py 
RUN apk add git 
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["api_test.py"]