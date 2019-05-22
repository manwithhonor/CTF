from flask import request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

from . import app
from .forms import HostForm, form_flash_errors
from .models import Host
from .utils import save_zip_to_hosting, save_new_hosting_item


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new', methods=['GET', 'POST'])
def new():
    host_form = HostForm()
    if request.method == 'POST' and host_form.validate_on_submit():
        domain = host_form.domain.data + '.reg.ctf'
        if not Host.objects(domain=domain).first():
            f = host_form.archive.data
            file_name = secure_filename(f.filename)
            file_path = os.path.join(
                app.config['TEMP_DIR'], file_name
            )
            f.save(file_path)
            out_path = os.path.join(app.config['WWW_DIR'], domain)

            if save_zip_to_hosting(file_path, out_path):
                save_new_hosting_item(domain=domain,
                     username=host_form.username.data,
                     password=host_form.password.data,
                     directory=out_path,
                     my_ip=app.config['MY_IP']
                     )
                return redirect(url_for('success', url=domain))
            else:
                flash("Error unzipping archive")
        else:
            flash("Domain is already registered", "danger")

    form_flash_errors(host_form)
    return render_template('new.html', form=host_form)


@app.route('/success/<url>')
def success(url):
    url = url
    return render_template('success.html', url=url, dns=app.config['MY_IP'])
