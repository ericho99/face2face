import unittest

from app import db
from app.models import User, StreamHosts, StreamViewers
from datetime import datetime

class ModelTest(unittest.TestCase):
	
	def test_User(self):
		u = User(username='brianli',psw='iamawesome',credit=0)
		u2 = User(username='Eric Ho',psw='imawesome',credit=5)
		u3 = User(username='Soy Lee',psw='soylee',credit=3.6)
		u4 = User(username='David',psw='d',credit=0)
		u5 = User(username='Tony',psw='psiwhat',credit=100000000)

		self.assertEquals("imawesome", u2.psw)
		self.assertEquals(3.6, u3.credit)

	def test_StreamHosts(self):
		h = StreamHosts(start_time=datetime(2015, 4, 19, 13, 0),
			end_time=datetime(2015, 4, 19, 15, 0), stream_price=500,
			stream_name="Cooking People")
		self.assertEquals(500, h.stream_price)
		self.assertEquals("Cooking People", h.stream_name)

	def test_StreamViewers(self):
		v = StreamViewers(viewer_id=1,stream_id=1,
			join_time=datetime(2015, 4, 19, 13, 20),
			leave_time=datetime(2015, 4, 19, 13, 25),viewer_rating=3)
		self.assertEquals(3, v.viewer_rating)
		self.assertEquals(datetime(2015, 4, 19, 13, 20), v.join_time)

	def test_foreign_host_key(self):
		h = StreamHosts(start_time=datetime(2015, 4, 19, 13, 0),
			end_time=datetime(2015, 4, 19, 15, 0), stream_price=500,
			stream_name="Cooking Peoples")
		
		db.session.add(h)
		db.session.commit()

		foreign_id = StreamHosts.query.filter_by(stream_name = "Cooking Peoples").first().id
		v = StreamViewers(viewer_id=1,stream_id=foreign_id,
			join_time=datetime(2015, 4, 19, 13, 20),
			leave_time=datetime(2015, 4, 19, 13, 25),viewer_rating=3)
		
		self.assertEquals(h.id, v.stream_id)
		
		db.session.delete(h)
		db.session.commit()

	def test_foreign_user_key(self):
		u = User(username='Swag',psw='cashmoney',credit=1000000000)
		
		db.session.add(u)
		db.session.commit()
		
		foreign_id = User.query.filter_by(username = "Swag").first().id
		v = StreamViewers(viewer_id=foreign_id,stream_id=1,
			join_time=datetime(2015, 4, 19, 13, 20),
			leave_time=datetime(2015, 4, 19, 13, 25),viewer_rating=3)
		
		self.assertEquals(u.id, v.viewer_id)
		
		db.session.delete(u)
		db.session.commit()

	def test_times(self):
		h = StreamHosts(start_time=datetime(2015, 4, 19, 13, 0),
			end_time=datetime(2015, 4, 19, 15, 0), stream_price=500,
			stream_name="Cooking People")

		v = StreamViewers(viewer_id=1,stream_id=1,
			join_time=datetime(2015, 4, 19, 13, 20),
			leave_time=datetime(2015, 4, 19, 13, 25),viewer_rating=3)

		self.assertEquals(datetime(2015, 4, 19, 13, 0), h.start_time)
		self.assertEquals(datetime(2015, 4, 19, 15, 0), h.end_time)
		self.assertEquals(datetime(2015, 4, 19, 13, 20), v.join_time)
		self.assertEquals(datetime(2015, 4, 19, 13, 25), v.leave_time)

	def test_username(self):
		u = User(username='chucknorris',psw='roundhouse',credit=3.6)
		self.assertEquals(type(u.username), str)
		self.assertEquals(u.username, "chucknorris")

	def test_streamname(self):
		h = StreamHosts(start_time=datetime(2015, 4, 19, 13, 0),
			end_time=datetime(2015, 4, 19, 15, 0), stream_price=500,
			stream_name="Cook Time")
		
		db.session.add(h)
		db.session.commit()

		foreign_id = StreamHosts.query.filter_by(stream_name = "Cook Time").first().id

		v = StreamViewers(viewer_id=1,stream_id=foreign_id,
			join_time=datetime(2015, 4, 19, 13, 20),
			leave_time=datetime(2015, 4, 19, 13, 25),viewer_rating=3)

		host_of_interest = StreamHosts.query.get(v.stream_id)
		self.assertEquals(host_of_interest.stream_name, "Cook Time")

		db.session.delete(h)
		db.session.commit()
	
	def test_keys(self):
		u = User(username='brianli',psw='iamawesome',credit=0)
		
		db.session.add(u)
		db.session.commit()
		
		h = StreamHosts(start_time=datetime(2015, 4, 19, 13, 0),
			end_time=datetime(2015, 4, 19, 15, 0), stream_price=500,
			stream_name="Cook Time")
		
		db.session.add(h)
		db.session.commit()

		foreign_id = StreamHosts.query.filter_by(stream_name = "Cook Time").first().id

		v = StreamViewers(viewer_id=1,stream_id=foreign_id,
			join_time=datetime(2015, 4, 19, 13, 20),
			leave_time=datetime(2015, 4, 19, 13, 25),viewer_rating=3)

		db.session.add(v)
		db.session.commit()

		self.assertEquals(type(u.id), int)
		self.assertEquals(type(h.id), int)
		self.assertEquals(type(v.id), int)
		self.assertEquals(u.id >= 0, True)
		self.assertEquals(h.id >= 0, True)
		self.assertEquals(v.id >= 0, True)
		
		db.session.delete(u)
		db.session.delete(v)
		db.session.delete(h)
		db.session.commit()
	
	def test_User_FieldTypes(self):
		u = User(username='brianli',psw='iamawesome',credit=0.0)		
	
		self.assertEquals(type(u.username), str)
		self.assertEquals(type(u.psw), str)
		self.assertEquals(type(u.credit), float)
		
	def test_StreamHost_FieldTypes(self):
		h = StreamHosts(start_time=datetime(2015, 4, 19, 13, 0),
			end_time=datetime(2015, 4, 19, 15, 0), stream_price=500.0,
			stream_name="Cook Time")

		self.assertEquals(type(h.start_time), datetime)
		self.assertEquals(type(h.end_time), datetime)
		self.assertEquals(type(h.stream_price), float)
		self.assertEquals(type(h.stream_name), str)

	def test_StreamViewers_FieldTypes(self):

		v = StreamViewers(viewer_id=1,stream_id=1,
			join_time=datetime(2015, 4, 19, 13, 20),
			leave_time=datetime(2015, 4, 19, 13, 25),viewer_rating=3)

		self.assertEquals(type(v.viewer_id), int)
		self.assertEquals(type(v.stream_id), int)
		self.assertEquals(type(v.join_time), datetime)
		self.assertEquals(type(v.leave_time), datetime)
		self.assertEquals(type(v.viewer_rating), int)

if __name__ == '__main__':
    unittest.main()