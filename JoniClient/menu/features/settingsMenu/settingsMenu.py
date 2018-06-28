# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import the needed classes:
# navigableMenuOption 			: The mother class
# settingsPreferredCategories 	: a sub option
# joniConfig 					: global configuration files
from menu.navigableMenuOption import NavigableMenuOption
from settingsPreferredCategories import SettingsPreferredCategories
import config.joniConfig as joniConfig



# This is the settings menu class, from which the user will be able to:
#	- set its preferred categories
class SettingsMenu(NavigableMenuOption):
	__metaclass__ = ABCMeta

	# class constructor
	# ---- super class constructor options ----
	# @optionName the name of this option ("mainMenu", "settings", ...)
	# @optionNameAudioPath the path to the .mp3 file reproducing the name of this option
	# @previousMenuOption the reference to the object representing the previous menu option 
	# @followingMenuOptions the reference to the list of objects representing the following menu options 
	# @inputEventManager the global inputEventManager object
	# @audioPlayer the global audioPlayer object
	# ---- class constructor ----
	# nothing
	
	def __init__(self, optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer):
		
		# to call the mother class init
		super(SettingsMenu, self).__init__(optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer)

	

	# to string method
	def toString( self ):
		return ("The only SettingsMenu in the world :D")



	# initialize the folowing options for this menu
	# note: Later on this list of options will be retrieved from a static file, and not hardcoded here)
	# @return self : this class, in order to be able to concatenate functions 
	def initializeFollowingOptions( self ):

		# if we don't have already initialized the following options list
		if (not self.alreadyInitializedOptions) :

			# the initialization of the sub options
			preferredCategories = SettingsPreferredCategories("SettingsMenuPreferredCategories", joniConfig.settingsPreferredCategoriesAudioPath, self, None, self.inputEventManager, self.audioPlayer);
			self.setFollowingMenuOptions([preferredCategories])

			self.alreadyInitializedOptions = True

		# return self
		return self