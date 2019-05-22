import base64
import re
from mongoengine import Q
from .models import Host
import logging

def encode_token(user, password):
    return base64.b64encode(user.encode() + b':' + password.encode())


def decode_token(token):
    auth_decoded = base64.b64decode(token)
    user, password = auth_decoded.split(b':', 2)
    return user.decode(), password.decode()


def check_user(user, password, host):
    item = Host.objects.filter(((Q(username=user) or Q(domain=host)) and (Q(password=password) or Q(domain=host)))).first()
    if item:
        enc = encode_token(user, password)
        return enc


def check_host(host):
    regex = re.compile('.*{}.*'.format(re.escape(host)))
    return Host.objects(domain=regex).first()
