# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import the needed classes:
# NavigableMenuOption 	: The mother class
# newsMenu 				: The news menu
# settingsMenu 			: The settings menu
# joniConfig 			: general file containing configuration values
from navigableMenuOption import NavigableMenuOption
from menu.features.newsFeature.newsMenu import NewsMenu
from menu.features.settingsMenu.settingsMenu import SettingsMenu
import config.joniConfig as joniConfig


# This is the news feature class
class MainMenu(NavigableMenuOption):
	__metaclass__ = ABCMeta

	# class constructor
	# ---- super class constructor ----
	# @optionName the name of this option ("mainMenu", "settings", ...)
	# @optionNameAudioPath the path to the .mp3 file reproducing the name of this option
	# @previousMenuOption the reference to the object representing the previous menu option 
	# @followingMenuOptions the reference to the list of objects representing the following menu options 
	# @inputEventManager the global inputEventManager object
	# ---- class constructor ----
	# nothing

	def __init__(self, optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer):
		
		# to call the mother class init
		super(MainMenu, self).__init__(optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer)



	# to string method
	def toString( self ):
		return ("The only MainMenu in the world :D")
	


	# initialize the folowing options for this menu
	# note: this is not done in the class constructor, because
	# otherwise there would be a chain effect, and all menus 
	# would be instantiated (probable waste of resources)
	# @return self : this class, in order to be able to concatenate functions 
	def initializeFollowingOptions( self ):

		# if we don't have already initialized the following options list
		if (not self.alreadyInitializedOptions) :

			# the initialization of the sub options
			newsMenu = NewsMenu("NewsMenu", joniConfig.newsMenuAudioPath, self, None, self.inputEventManager, self.audioPlayer);
			settingsMenu = SettingsMenu("SettingsMenu", joniConfig.settingsMenuAudioPath, self, None, self.inputEventManager, self.audioPlayer);
			
			self.setFollowingMenuOptions([newsMenu, settingsMenu])

			self.alreadyInitializedOptions = True

		# return self
		return self
