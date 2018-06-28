# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import the needed classes:
# navigableMenuOption 	: The mother class
# newsCategories 		: a sub option 
from menu.navigableMenuOption import NavigableMenuOption
from newsCategories import NewsCategories
import config.joniConfig as joniConfig


# This is the news feature class
class NewsMenu(NavigableMenuOption):
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
		super(NewsMenu, self).__init__(optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer)



	# to string method
	def toString( self ):
		return ("The only NewsMenu in the world :D")



	# initialize the folowing options for this menu
	# note: Later on the construction of this list of options will be
	# optimized by integrating local data with new one from the server
	# @return self : this class, in order to be able to concatenate functions 
	def initializeFollowingOptions( self ):

		# if we don't have already initialized the following options list OR there are new categories
		if (not self.alreadyInitializedOptions or joniConfig.areThereNewCategories) :

			# reproduce the downloadInProgressAudioPath audio
			self.audioPlayer.reproduceAudio(joniConfig.downloadInProgressWithMusicAudioPath)

			# get the list of user preferred categories from the server
			preferredCategories = joniConfig.api.getUserPreferredCategories(joniConfig.user)

			# temporary variable for the lists of categories
			listOfCategories = []

			# for each defined category
			for i in range(len(preferredCategories)):

				# create the related newsCategory object
				newCategory = NewsCategories(preferredCategories[i]['name'], preferredCategories[i]['nameAudioPath'], self, None, self.inputEventManager, self.audioPlayer, False, None);
				
				# append it to the list
				listOfCategories.append(newCategory)

			# set (or reset) the following menu options
			self.setFollowingMenuOptions(listOfCategories)

			self.alreadyInitializedOptions = True
			joniConfig.areThereNewCategories = False

		# return self
		return self