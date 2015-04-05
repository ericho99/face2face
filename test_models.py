import unittest

from app import db
from app.models import User, StreamHosts, StreamViewers

class ModelTest(unittest.TestCase):
	
	def test_User(self):
		u = User(username='brianblowspeen',psw='dickbutt',credit=0)
		u2 = User(username='Eric Ho',psw='imawesome',credit=5)
		u3 = User(username='Soy Lee',psw='soylee',credit=3.6)
		u4 = User(username='David',psw='d',credit=0)
		u5 = User(username='Tony',psw='psiwhat',credit=100000000)

		self.assertEquals("brianblowspeen", u.username)
		self.assertEquals("imawesome", u2.psw)
		self.assertEquals(3.6, u3.credit)

	def test_StreamHosts(self):
		h = StreamHosts(start_time="1:00",end_time="3:00",stream_price=500,stream_name="Cooking People")

		self.assertEquals(500, h.stream_price)
		self.assertEquals("1:00", h.start_time)

	def test_StreamViewers(self):
		v = StreamViewers(viewer_id=1,stream_id=1,join_time="1:20",leave_time="1:25",viewer_rating=3)

		self.assertEquals(3, v.viewer_rating)
		self.assertEquals("1:20", v.join_time)
		#would be good to test if viewer_id / stream_id reference correct viewer/host

if __name__ == '__main__':
    unittest.main()