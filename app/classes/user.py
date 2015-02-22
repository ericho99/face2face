import datetime
class User:
	def __init__(self, username, psw, fname, lname, b_month, b_day, b_year, credit_num = "",
				 payment_type = "", prof_pic = ""):
	# consider adding more info/different data types
		self.psw = psw
		self.username = username # should be hashed
		self.fname = fname
		self.lname = lname
		self.birthday = datetime.date(b_year, b_month, b_day)
		self.credit_num = credit_num # should be hashed
		self.payment_type = payment_type
		self.prof_pic = prof_pic # currently url assumed; subject to change
	def check_login(username, psw):
	# might want to define elsewhere
		if (username == self.username and psw == self.psw):
			return True
		else:
			return False