# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import the needed classes:
# NavigableMenuOption 	: The mother class
# News 		 			: The news class  
# joniConfig 			: global config file
from menu.navigableMenuOption import NavigableMenuOption
from menu.features.newsFeature.news import News
import config.joniConfig as joniConfig


# This is the news feature class
class NewsTitles(NavigableMenuOption):
	__metaclass__ = ABCMeta

	# class constructor
	# ---- super class constructor options ----
	# @optionName the name of this option ("mainMenu", "settings", ...)
	# @optionNameAudioPath the path to the .mp3 file reproducing the name of this option
	# @previousMenuOption the reference to the object representing the previous menu option 
	# @followingMenuOptions the reference to the list of objects representing the following menu options 
	# @inputEventManager the global inputEventManager object
	# ---- class constructor ----
	# nothing

	def __init__(self, optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer):

		# to call the mother class init
		super(NewsTitles, self).__init__(optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer)


	# to string method
	def toString( self ):
		return ("NewsTitle ID: " + self.optionName)


	# Download the audio of the news and set it as following options
	# @return self : this class, in order to be able to concatenate functions 
	def initializeFollowingOptions( self ):

		# reproduce the downloadInProgressAudioPath audio
		self.audioPlayer.reproduceAudio(joniConfig.downloadInProgressWithMusicAudioPath)

		print "news title " + self.optionName + " is initializeFollowingOptions"

		# get the news description audio
		newsDescription = joniConfig.api.getNewsByNewsId(joniConfig.user,self.optionName)

		print "this is the newsDescription from the server"
		print newsDescription

		# compose the path to the news description audio
		pathToNewsDescriptionAudio = joniConfig.newsBaseDirectoryAudioPath + "descriptions/" + self.optionName + ".mp3"

		# create the related news object
		newNews = News(self.optionName, pathToNewsDescriptionAudio, self, None, self.inputEventManager, self.audioPlayer)

		# set (or reset) the following menu options
		self.setFollowingMenuOptions([newNews])

		# return self
		return self



	# if the user pushes the play button, we do not enter in a submenu
	# Instead, we reproduce the audio of the description of the news
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputPlay( self ):

		# just stay where we are and reproduce the news description audio
		return self.reproduceOptionAudio(None)



	# if the user pushes the backward button, change news title
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputBackward( self ):

		super(NewsTitles, self).handleInputReturn()
		return self.previousMenuOption.handleInputBackward();



	# if the user pushes the backward button, change news title
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputForward( self ):

		super(NewsTitles, self).handleInputReturn()
		return self.previousMenuOption.handleInputForward();



	# reproduce audio
	# usually this method is used to reproduce the audio associated with the menu options
	# @param audio : the path to the audio to be reproduced. if None, reproduce the first option audio. 
	# @return self : this class, in order to be able to concatenate functions 
	def reproduceOptionAudio( self, audio ):

		# if no audio was provided
		if (audio == None or audio == "MenuIntro"):

			# if there are no options available
			if (self.followingMenuOptions == None):
				
				# set the audio to be reproduced to noOptionAvailable
				audio = joniConfig.noMenuOptionAvailableAudioPath

			# otherwise, there is at least an option in the following option menu
			else:

				# reproduce its name
				audio = self.followingMenuOptions[self.currentMenuOptionIndex].optionNameAudioPath

		# reproduce the audio file through the proper audio module
		self.audioPlayer.reproduceAudio(audio)

		# return self
		return self