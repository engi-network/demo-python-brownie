FROM docker.io/python:3.9

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

RUN npm install ganache --global

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt