from app import db
from datetime import datetime

# Next steps:
#   -Data validation
#   -Create views
#   -See where we can integrate frontend

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(26))
    email = db.Column(db.String(26))
    psw = db.Column(db.String(26)) # encrypt or hash
    credit = db.Column(db.Float)
    paypal_username = db.Column(db.String(26))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '#%d: username: %s password: %s credit: %d paypal_username: %s'\
            % (self.id,self.username,self.psw,self.credit,self.paypal_username)

class StreamHosts(db.Model):
    __tablename__ = 'stream_hosts'
    
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    stream_price = db.Column(db.Float)
    stream_number = db.Column(db.Integer) #hashed stream number
    stream_name = db.Column(db.String(26))
    description = db.Column(db.String(200))
    embed_url = db.Column(db.String(100))
    host_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
         return '#%d: host: %d streamnumber: %d streamname: %s description: %s stream_price: %f url: %s'\
            % (self.id,self.host_id,self.stream_number,self.stream_name,self.description,self.stream_price,self.embed_url)

class StreamViewers(db.Model):
    __tablename__ = 'stream_viewers'
    
    id = db.Column(db.Integer, primary_key=True)
    viewer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    stream_id = db.Column(db.Integer, db.ForeignKey('stream_hosts.id'))
    join_time = db.Column(db.DateTime)
    leave_time = db.Column(db.DateTime)
    viewer_rating = db.Column(db.Integer)
    
    def __repr__(self):
        return '#%d: viewer_id: %d stream_id: %d joined: %s quit: %s rating: %d'\
            % (self.id, self.viewer_id, self.stream_id, self.join_time, 
                self.leave_time, self.viewer_rating)


