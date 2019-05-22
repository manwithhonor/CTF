from . import db


class Host(db.Document):
    domain = db.StringField(max_length=100, required=True)
    directory = db.StringField(max_length=255, required=True)
    username = db.StringField(max_length=100, required=True)
    password = db.StringField(max_length=100, required=True)

    def __repr__(self):
        return self.domain + ' @ ' + self.directory
