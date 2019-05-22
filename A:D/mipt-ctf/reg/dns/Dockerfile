FROM python:3.6-alpine

ADD ./requirements.txt /home/root/requirements.txt

RUN pip install -r /home/root/requirements.txt

ADD ./dnserver.py /home/root/dnserver.py
ADD ./config.py /home/root/config.py


EXPOSE 53/tcp
EXPOSE 53/udp
CMD ["/home/root/dnserver.py"]
