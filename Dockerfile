# start from base
FROM python:3.6

MAINTAINER Faizan Shaikh  <sentry88prime@gmail.com>
# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src/manage.py ./

EXPOSE 8000
CMD [ "python", "manage.py","runserver" ]