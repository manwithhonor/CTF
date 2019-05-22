FROM debian:latest

RUN apt-get update \
&& apt-get install -y libgmp-dev build-essential python3 python3-setuptools python3-pip python3-virtualenv

WORKDIR /app


ADD requirements.txt /app/requirements.txt

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
RUN pip3 install gunicorn

ADD app /app/app
ADD wsgi.py /app/wsgi.py

EXPOSE 8004

CMD ["gunicorn", "--bind", "0.0.0.0:8004","-w", "2", "wsgi"]
