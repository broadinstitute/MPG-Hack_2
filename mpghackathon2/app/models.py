from app import db

class Protocol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    protocol_description = db.Column(db.String(1024), index=True, unique=True)

    def __repr__(self):
        return '<Title %r>' % (self.title)
