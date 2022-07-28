FROM python:3.8.5-slim-buster
MAINTAINER babajung <babajung@gmail.com>

ARG BUILD_DATE
ARG VCS_REF

# Set labels (see https://microbadger.com/labels)
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/babajung/python3-slim-buster-flask-usecase3a"

# RUN apt-get -y install libc-dev
# RUN apt-get -y install build-essential

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
# COPY *.py /usr/src/app
# COPY *.yaml /usr/src/app
# COPY static/ /usr/src/app/static/
# COPY templates/ /usr/src/app/templates/

# Expose the Flask port
EXPOSE 5000

CMD [ "python", "./app.py" ]