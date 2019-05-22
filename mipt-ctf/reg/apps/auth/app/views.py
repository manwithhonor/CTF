from flask import abort, make_response, redirect, render_template, request

from . import app
from .forms import LoginForm
from .utils import check_user, decode_token, check_host


@app.route('/', methods=['GET'])
def authenticate():
    token = request.cookies.get('token')
    host = request.headers.get('Host', '')
    if token is None:
        abort(401)
    username, password = decode_token(token)
    if check_user(username, password, host) is not None:
        # Add headers to be authenticated with services
        resp = make_response()
        resp.headers['REMOTE_USER'] = username
        resp.headers['X-WEBAUTH-USER'] = username
        return resp
    abort(401)


@app.route('/login', methods=['GET', 'POST'])
def login():
    target = request.headers.get('X-Original-URI', '/')
    host = request.headers.get('Host', '')
    host = host.split(':')[0]
    check_result = check_host(host)
    if not check_result:
        return "Host not found: %s" % host
    host = check_result.domain

    form = LoginForm(target=target)
    if form.validate_on_submit():
        username = form.login.data
        password = form.password.data
        target = form.target.data
        auth_token = check_user(username, password, host)
        if auth_token:
            resp = make_response(redirect(target))

            resp.set_cookie('token', auth_token,
                            secure=False,
                            httponly=True,
                            )

            resp.headers['REMOTE_USER'] = username
            resp.headers['X-WEBAUTH-USER'] = username
            resp.headers['X-Forwarded-User'] = username
            return resp
    return render_template('login.html', form=form, website=host)


if __name__ == '__main__':
    app.run()
