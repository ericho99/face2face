from app import db


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(26))
    credit = db.Column(db.Integer)

    # panlist_id = db.Column(db.Integer, db.ForeignKey('panlists.id'))

    def __repr__(self):
        return '#%d: name: %s credit_card: %d' % (self.id, self.name, self.credit)

class Stream(db.Model):
	__tablename__ = 'streams'
	id = db.Column(db.Integer, primary_key=True)
	stream = db.Column(db.Integer) #hashed stream number
	name = db.Column(db.String(26))
	description = db.Column(db.String(200))
	url = db.Column(db.String(100))
	# owner id
	# authenticated viewer table

	def __repr__(self):
		return '#%d: streamnumber: %d name: %s description: %s url: %s' % (self.id, self.stream, self.name, self.description, self.url)