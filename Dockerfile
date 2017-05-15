FROM ubuntu:latest

MAINTAINER Julian Theoderik Trajanson "julian.trajanson@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential lsof

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["run.py"]

EXPOSE 8000
EXPOSE 5000
