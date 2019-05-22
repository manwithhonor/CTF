from flask_wtf import FlaskForm
from flask import flash
from flask_wtf.file import FileField, FileRequired, FileAllowed, StopValidation, FileStorage
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp


def form_flash_errors(form: FlaskForm) -> None:
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


# Experimental validator from https://github.com/lepture/flask-wtf/pull/309
class FileMaxSize(object):
    """Validates that the uploaded file is within a maximum file size given in bytes
    :param max_size: maximum file size given in kilobytes
    :param message: error message
    You can also use the synonym ``file_max_size``.
    """

    def __init__(self, max_size, message=None):
        self.max_size = max_size
        self.message = message

    def __call__(self, form, field):
        if not (isinstance(field.data, FileStorage) and field.data):
            return

        file_size = len(field.data.read()) / 1024  # read the file to determine its size and convert from bytes to Kb
        field.data.seek(0)  # reset cursor position to beginning of file

        if file_size <= self.max_size:
            return
        else:  # the file is too big => validation failure
            raise StopValidation(self.message or field.gettext(
                'File should be smaller than ' + str(self.max_size) + ' Kb.'
            ))


class HostForm(FlaskForm):
    domain = StringField('Domain',
                         validators=[Regexp('^[a-z0-9\-]{0,100}$',
                                            message='Domain must be shorter than 100 chars and only contain a-z, '
                                                    '0-9 and "-"'
                                            )
                                     ]
                         )
    username = StringField('Username', validators=[DataRequired(message='Username is a required field.')])
    password = PasswordField('Password', validators=[DataRequired(message='Password is a required field')])
    archive = FileField(validators=[FileRequired(),
                                    FileAllowed(['zip'], 'ZIP Archives only.'),
                                    FileMaxSize(100)
                                    ]
                        )
