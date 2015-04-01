from app import app
from app.models import *

db.drop_all()
db.create_all()

p = Person(name='Eric',credit=123412)
db.session.add(p)
db.session.commit()