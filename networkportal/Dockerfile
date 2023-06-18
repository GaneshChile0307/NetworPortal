FROM ubuntu:20.04

RUN apt-get update && apt-get install -y tzdata && apt install -y python3.9 python3-pip python3.9-dev libmysqlclient-dev

RUN apt install python3-dev libpq-dev nginx -y

WORKDIR /app

COPY . .

COPY requirements.txt .


RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "networkportal.wsgi"]