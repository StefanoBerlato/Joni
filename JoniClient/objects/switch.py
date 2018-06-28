# This is the Switch class which represents the physical switches
class Switch():


	# class constructor. Just assigns the button name and the pin number
	def __init__(self, switchName, switchPinNumber):
		self.switchName = switchName
		self.switchPinNumber = switchPinNumber


	# toString method
	def toString(self):
		return ("This is switch " + self.switchName + " with pin number " + self.switchPinNumber)


	# get switch name method
	# @return switchName : the name associated to this switch
	def getSwitchName (self):
		return self.switchName


	# get switch pin number
	# @return switchPinNumber : the number of the pin associated to this switch
	def getSwitchPinNumber (self):
		return self.switchPinNumber