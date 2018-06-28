# This is the User class which represents the user
class User():


	# class constructor. Just assigns the button name and the pin number
	def __init__(self, userId):
		self.userId = userId

	# toString method
	def toString(self):
		return ("This is userId " + self.userId)


	# get button name method
	def getUserId (self):
		return self.userId
