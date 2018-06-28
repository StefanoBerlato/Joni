# This is the Button class which represents the physical buttons
class Button():


	# class constructor. Just assigns the button name and the pin number
	def __init__(self, buttonName, buttonPinNumber):
		self.buttonName = buttonName
		self.buttonPinNumber = buttonPinNumber


	# toString method
	def toString(self):
		return ("This is button " + self.buttonName + " with pin number " + self.buttonPinNumber)


	# get button name method
	# @return buttonName : the name associated to this button
	def getButtonName (self):
		return self.buttonName


	# get button pin number
	# @return buttonPinNumber : the number of the pin associated to this button
	def getButtonPinNumber (self):
		return self.buttonPinNumber