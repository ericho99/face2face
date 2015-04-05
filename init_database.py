from app import app
from app.models import *

db.drop_all()
db.create_all()

u = User(username='brianblowspeen',psw='dickbutt',credit=0)
u2 = User(username='ericho',psw='imawesome',credit=5)
u3 = User(username='soylee',psw='soylee',credit=3.6)
u4 = User(username='David',psw='d',credit=0)
u5 = User(username='A',psw='a',credit=100000000)

db.session.add(u)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.add(u5)
db.session.commit()

host_id = User.query.filter(User.username=='brianblowspeen').first().id
s = StreamHosts(start_time=datetime(2015,4,5,1,30),end_time=datetime(2015,4,5,3,30),stream_price=1.2,stream_number=19836581,stream_name='brians cooking show',description='brian is cooking and shit',embed_url='https://www.youtube.com/watch?v=Zw8iljkD1So',host_id=host_id)
db.session.add(s)
db.session.commit()

stream_id = s.id
viewer_id = User.query.filter(User.username=='ericho').first().id
viewer_id2 = User.query.filter(User.username=='A').first().id
#null viewer rating for now
v = StreamViewers(viewer_id=viewer_id,stream_id=stream_id,join_time=datetime(2015,4,5,1,00),leave_time=datetime(2015,4,5,4,00))
db.session.add(v)
db.session.commit()
