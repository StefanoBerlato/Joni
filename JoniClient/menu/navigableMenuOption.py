	# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import the needed classes:
# InputEventReceiver 	: The mother class
# InputEventManager 	: The class that handles the user events, button and switches
# AudioPlayer 			: The class that handles the audio streams
# joniConfig 			: general file containing configuration values
from util.inputEventReceiver import InputEventReceiver
from util.inputEventManager import InputEventManager
from util.audioPlayer import AudioPlayer
import config.joniConfig as joniConfig


# This is the class from which every menu element class should inherit
# It handles the simple navigation through the menu
# It implements play - return - backward - forward - volume up - volume down
class NavigableMenuOption(InputEventReceiver):
	__metaclass__ = ABCMeta


	# class constructor
	# @param optionName : the name of this option ("mainMenu", "settings", ...)
	# @param optionNameAudioPath : the path to the .mp3 file reproducing the name of this option
	# @param previousMenuOption : the reference to the object representing the previous menu option 
	# @param followingMenuOptions : the reference to the list of objects representing the following menu options 
	# @param inputEventManager : the global inputEventManager object
	# @param AudioPlayer : the class that handles the audio streams
	def __init__(self, optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, AudioPlayer):
		
		# to call the mother class init method
		super(NavigableMenuOption, self).__init__()

		# assigning the given the variables
		self.optionName = optionName
		self.optionNameAudioPath = optionNameAudioPath
		self.previousMenuOption = previousMenuOption
		self.followingMenuOptions = followingMenuOptions
		self.inputEventManager = inputEventManager
		self.audioPlayer = AudioPlayer

		# the index of the current option considered in the list of following options
		self.currentMenuOptionIndex = 0

		# did we initialized the following options?
		self.alreadyInitializedOptions = False



	# to string method
	def toString( self ):
		return ("This is NavigableMenuOption " + self.optionName)



	# set the list of the following menu options
	# @param followingMenuOptions : the list of following options OR the string "waiting" 
	# to reproduce the "download In Progress" audio 
	# @return self : this class, in order to be able to concatenate functions 
	def setFollowingMenuOptions( self, followingMenuOptions ):

		# if we receive an empty list
		if (followingMenuOptions == []):

			# consider it as None
			followingMenuOptions = None

		# now set the value to the class variable
		self.followingMenuOptions = followingMenuOptions

		# return self
		return self


	# set the reference to the previous menu option
	# @param previousMenuOption : the previous menu option
	# @return self : this class, in order to be able to concatenate functions 
	def setPreviousMenuOption( self, previousMenuOption ):

		# set which is the previous option in the menu tree
		self.previousMenuOption = previousMenuOption

		# return self
		return self


	# reproduce audio
	# usually this method is used to reproduce the audio associated with the menu options
	# @param audio : the path to the audio to be reproduced. if None, reproduce the first option audio. If "MenuIntro", play the menu intro 
	# @return self : this class, in order to be able to concatenate functions 
	def reproduceOptionAudio( self, audio ):
		print audio
		# if no audio was provided
		if (audio == None):

			# if there are no options available
			if (self.followingMenuOptions == None):
				
				# set the audio to be reproduced to noOptionAvailable
				audio = joniConfig.noMenuOptionAvailableAudioPath

			# otherwise, there is at least an option in the following option menu
			else:

				# reproduce its name
				audio = self.followingMenuOptions[self.currentMenuOptionIndex].optionNameAudioPath

		# if we have to reproduce the intro of this menu
		elif (audio == "MenuIntro"):

				# reproduce the intro
				audio = joniConfig.menuBaseDirectoryAudioPath + self.optionName + ".mp3"


		# reproduce the audio file through the proper audio module
		self.audioPlayer.reproduceAudio(audio)

		# return self
		return self



	# if the user pushes the play button
	# usually this enter in the selected menu option
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputPlay( self ):

		# if there are not further options
		if (self.followingMenuOptions == None):

			# just stay where we are and reproduce the noOptionAvailable audio
			self.reproduceOptionAudio(joniConfig.noMenuOptionAvailableAudioPath)

		# else
		else:

			# make the selected Option object to initialize its submenu
			self.followingMenuOptions[self.currentMenuOptionIndex].initializeFollowingOptions();

			# set the event receiver to be the following selected Option object
			self.inputEventManager.setEventReceiver(self.followingMenuOptions[self.currentMenuOptionIndex])

		# return self
		return self


	# if the user pushes the return button
	# usually this return to the previous option in the tree menu
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputReturn( self ):

		# if this is the root menu
		if (self.previousMenuOption == None):

			# just reproduce its name
			self.reproduceOptionAudio(None)

		# if this is NOT the root menu
		else:
			
			# reset the option index for this submenu 
			self.currentMenuOptionIndex = 0

			# set the event receiver to be the previous Option object
			self.inputEventManager.setEventReceiver(self.previousMenuOption)

		# return self
		return self



	# if the user pushes the backward button
	# Usually this scroll the list of menu options backwardly
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputBackward( self ):

		# if there are following menu options
		if (not self.followingMenuOptions == None):

			# navigate to the previous option substracting 1 to the index
			self.currentMenuOptionIndex = self.currentMenuOptionIndex - 1

			# if the user goes back the first option 
			if (self.currentMenuOptionIndex < 0):

				# return the last one
				self.currentMenuOptionIndex = len (self.followingMenuOptions) - 1

			# reproduce its name
			self.reproduceOptionAudio(None)

		# otherwise, this is a leaf of the menu tree 
		else:

			# just reproduce its name
			self.reproduceOptionAudio(joniConfig.noMenuOptionAvailableAudioPath)
		
		# return self
		return self



	# if the user pushes the backward button
	# Usually this scroll the list of menu options backwardly
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputForward( self ):

		# if there are following menu options
		if (not self.followingMenuOptions == None ):

			# navigate to the next option modularly adding 1 to the index
			self.currentMenuOptionIndex = (self.currentMenuOptionIndex + 1) % len (self.followingMenuOptions)

			# reproduce its name
			self.reproduceOptionAudio(None)

		# otherwise, this is a leaf of the menu tree 
		else:
			
			# just reproduce its name
			self.reproduceOptionAudio(joniConfig.noMenuOptionAvailableAudioPath)
		
		# return self
		return self



	# if the user pushes the volume up button
	# call the method from the audioPlayer class
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputVolumeUp( self ):

		print( self.toString() + ": volume up")	# debug

		# increase the volume
		self.audioPlayer.increaseAudioVolume();

		# return self
		return self



	# if the user pushes the volume down button
	# call the method from the audioPlayer class
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputVolumeDown( self ):

		print( self.toString() + ": volume down")	# debug

		# decrease the volume
		self.audioPlayer.decreaseAudioVolume();

		# return self
		return self



	# this is the method whose implementation will differentiate the various menu options
	# this method is automatically invoked when acceding the menu option for the first time
	# this method is invoked by the handlePlayInput function
	@abstractmethod
	def initializeFollowingOptions( self ):
		pass