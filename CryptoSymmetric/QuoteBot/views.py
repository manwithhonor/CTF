from flask import Flask, render_template, request, make_response, redirect, url_for
from base64 import b64decode, b64encode
from functools import wraps
import os
from cryptoweb import app
from cryptoweb.SessionManager import Session
from cryptoweb.Flags import FLAG



def generate_default_session():
    session = Session()
    session.set_value(b'type', b'user')
    session.set_value(b'name', b'guest')
    return session


def session_handler(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logged = False
        if 'session' in request.cookies:
            try:
                request.session = Session(request.cookies.get('session'))
                logged = True
            except ValueError as v:
                logged = False

        if not logged:
            request.session = generate_default_session()

        result = f(*args, **kwargs)
        resp = make_response(result)
        try:
            resp.set_cookie('session', request.session.get_cookie())
            return resp
        except ValueError as e:
            return str(e), 500
    return decorated_function


@app.route('/', methods=['GET'])
@session_handler
def main():
    is_admin = request.session.get_value(b'type') == b'admin'

    name = request.session.get_value(b'name')
    flag = None    
    if is_admin:
        flag = FLAG()

    return render_template('index.html', flag=flag, name=name.decode())


@app.route('/quote', methods=['POST'])
@session_handler
def quote():
    try:
        command = b64decode(request.form['cmd']).decode()
        base_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'static',
            'quotes',
            command)
        base_path = os.path.realpath(base_path)
        if '/proc' in base_path or '/dev' in base_path:
            return "", 400
    except:
        return "", 400

    try:
        with open(base_path, 'rb') as f:
            return b64encode(f.read())
    except FileNotFoundError:
        base_path = os.path.join(*os.path.split(base_path)[:-1])


    try:
        lists = os.listdir(base_path)
        return b64encode(('Quote not found but here are some other you can listen to:' +
                          ', '.join(lists)).encode())

    except FileNotFoundError:
        return "", 400


@app.route('/change-name', methods=['POST'])
@session_handler
def change_name():
    name = request.form.get('name')

    if name:
        try:
            name = b64decode(name)
        except:
            return 'Incorrect input', 218

        if len(name) < 3 or len(name) > 100:
            return 'Name length should be in range [3, 100]', 218

        request.session.set_value(b'name', name)
        print(request.session.data)
        return '', 200

    return 'New name isn\'t specified', 218

