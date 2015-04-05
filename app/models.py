from app import db
import datetime

# Next steps:
#   -Data validation
#   -Create views
#   -See where we can integrate frontend

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(26))
    fname = db.Column(db.String(26))
    lname = db.Column(db.String(26))
    psw = db.Column(db.String(26)) # encrypt or hash
    credit = db.Column(db.Integer)
    paypal_username = db.Column(db.String(26))
    birthday = db.Column(db.Date)

    def __repr__(self):
        return '#%d: name: %s credit_card: %d' % (self.id, self.name, self.credit)

class StreamHosts(db.Model):
    __tablename__ = 'stream_hosts'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    stream = db.Column(db.Integer) #hashed stream number
    name = db.Column(db.String(26))
    description = db.Column(db.String(200))
    url = db.Column(db.String(100))
    host_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __repr__(self):
         return '#%d: streamnumber: %d name: %s description: %s url: %s' % \
            (self.id, self.stream, self.name, self.description, self.url)

class StreamViewers(db.Model):
    __tablename__ = 'stream_viewers'
    id = db.Column(db.Integer, primary_key=True)
    viewer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    stream_id = db.Column(db.Integer, db.ForeignKey('stream_hosts.id'))
    join_time = db.Column(db.DateTime)
    leave_time = db.Column(db.DateTime)
    viewer_rating = db.Column(db.Integer)
    def __repr__(self):
        return '#%d: viewer_id: %d stream_id: %d joined: %s quit: %s rating: ' % \
            (self.id, self.viewer_id, self.stream_id, self.join_time, 
                self.quit_time, self.viewer_rating)