from app import db


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(26))
    credit = db.Column(db.Integer)

    # panlist_id = db.Column(db.Integer, db.ForeignKey('panlists.id'))

    def __repr__(self):
        return '#%d: name: %s credit_card: %d' % (self.id, self.name, self.credit)