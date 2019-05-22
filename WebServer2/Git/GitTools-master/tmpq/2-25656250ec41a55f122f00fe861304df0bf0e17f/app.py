from flask import Flask, session
from functools import wraps

def auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            session['admin'] = False
        return f(*args, **kwargs)
    return decorated_function

app = Flask(__name__, static_folder='.git', static_url_path='/.git')
app.config.from_pyfile('config.py')

@app.route("/", methods=["GET"])
@auth
def main():
	is_admin = session.get('admin', False)
	if is_admin:
		return open('/flag').read()
	else:
		return "Service under development. Please try again later..."

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, threaded=True)
