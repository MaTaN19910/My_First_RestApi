FROM python:3.7




COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    gcc \
    python3-dev \


RUN mkdir /opt/my_first_restapi

WORKDIR /opt/my_first_restapi

ADD . .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]