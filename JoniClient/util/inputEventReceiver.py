# import the class that allows us to have interface classes
from abc import ABCMeta, abstractmethod

# This is the class from which every other class that has a direct
# interaction with the user (e.g. menu elements) should inherit
# the method names are self explaining
class InputEventReceiver:
	__metaclass__ = ABCMeta



	# class constructor
	def __init__(self):
		print("")


	def toString( self ):
		print ("The only InputEventReceiver in the world :D")



	@abstractmethod
	def handleInputPlay( self ):
		pass



	@abstractmethod
	def handleInputReturn( self ):
		pass



	@abstractmethod
	def handleInputBackward( self ):
		pass



	@abstractmethod
	def handleInputForward( self ):
		pass



	@abstractmethod
	def handleInputVolumeUp( self ):
		pass



	@abstractmethod
	def handleInputVolumeDown( self ):
		pass
