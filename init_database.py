from app import app
from app.models import *

db.drop_all()
db.create_all()

p = Person(name='Eric',credit=123412)
db.session.add(p)
db.session.commit()

s = Stream(stream=15,name='eric teaches cooking',description='eric is cool',url='https://www.youtube.com/watch?v=GSJ8c0lD_wk')
db.session.add(s)
db.session.commit()
