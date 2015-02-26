from user import User

class CheckLogin:
# we could change/refactor this class; just trying to get some code down.
# Not sure what we're going for; let's discuss at next meeting.
	
	# define users here: this assume users is a list of sample users

	def __init__(self, username, psw):
		self.username = username
		self.psw = psw
		self.usr = pass_match(self, users) # users will need to be something
										   # external
	def pass_match(self, users):
	# "users" could be a queried database of all users. This is just the basic
	# code that we should modify based on what we're actually using. I'm just
	# treating users as a list object for now.
		for usr in users:
			if (usr.username == self.username and usr.psw = self.psw):
				return usr
		return None # consider changing this return type

def sample_check():
# method that outlines what I'm going for; delete later
	userlogin = CheckLogin("bob", "sushi78woad_zDrank")
	if userlogin.usr: # None is false in an if statement
		print (userlogin.usr.fname + " " + userlogin.usr.fname " logged on.")
	else:
		print "User and password do not match."

