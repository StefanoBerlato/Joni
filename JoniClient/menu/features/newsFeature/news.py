# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import the needed classes:
# navigableMenuOption 	: The mother class
from menu.navigableMenuOption import NavigableMenuOption
import config.joniConfig as joniConfig


# This is the news feature class
class News(NavigableMenuOption):
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

		print "news " + optionName + " instantiated"

		# to call the mother class init
		super(News, self).__init__(optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer)


	# to string method
	def toString( self ):
		return ("News ID: " + self.optionName)


	# Since there are no sub options, just return
	# @return self : this class, in order to be able to concatenate functions 
	def initializeFollowingOptions( self ):

		# return self
		return self