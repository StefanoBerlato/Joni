# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import the needed classes:
# navigableMenuOption 	: The mother class
# newsCategories 		: to instantiate the categories classes to then be preferred 
from menu.navigableMenuOption import NavigableMenuOption
from menu.features.newsFeature.newsCategories import NewsCategories
import config.joniConfig as joniConfig


# This is the class that allows the user to choose which categories to prefer
class SettingsPreferredCategories(NavigableMenuOption):
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
		super(SettingsPreferredCategories, self).__init__(optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer)

		# this class will keep a list of flags (True or False) related to the status of the category (Enabled or Disabled) 
		self.isCategoryEnabled = None


	# to string method
	def toString( self ):
		return ("The only SettingsPreferredCategories in the world :D")



	# initialize the folowing options for this menu
	# note: Later on this list of options should be retrieved from a static file, and not hardcoded here)
	# @return self : this class, in order to be able to concatenate functions 
	def initializeFollowingOptions( self ):

		# reproduce the downloadInProgressAudioPath audio
		self.audioPlayer.reproduceAudio(joniConfig.downloadInProgressWithMusicAudioPath)

		# get the list of user preferred categories from the server
		preferredCategories = joniConfig.api.getUserPreferredCategories(joniConfig.user)

		# temporary variable for the lists of categories classes
		listOfCategories = []

		# is the category enabled (False by default)?
		self.isCategoryEnabled = [False, False, False, False, False, False, False]

		# for each preferred category 
		for i in range(len(preferredCategories)):

			# if the category is present in the preferred ones set its flags to "True", thus it is enabled
			self.isCategoryEnabled[joniConfig.categories.index(preferredCategories[i]['name'])] = True

		# for each category 
		for i in range(len(joniConfig.categories)):

			# instantiate a newsCategories classe
			newCategory = NewsCategories(joniConfig.categories[i], joniConfig.categoriesAudioPaths[i], self, None, 
										 self.inputEventManager, self.audioPlayer, True, self.isCategoryEnabled[i]);
			
			joniConfig.categoriesEnabled[joniConfig.categories[i]] = self.isCategoryEnabled[i]

			# and append it to the list of categories
			listOfCategories.append(newCategory)


		# set (or reset) the following menu options
		self.setFollowingMenuOptions(listOfCategories)

		# return self
		return self


	# if the user pushes the return button
	# send notification to the server of the new preferred categories
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputReturn( self ):

		# temporary variable for the lists of categories 
		listOfNewPreferredCategories = []

		print joniConfig.categoriesEnabled

		# for each category 
		for i in range(len(joniConfig.categories)):
 
			print joniConfig.categories[i]

			# if the category is present in the preferred ones
			if (joniConfig.categoriesEnabled[joniConfig.categories[i]]):

				# add it in the list of preferred ones
				listOfNewPreferredCategories.append(joniConfig.categories[i])

				print "		enabled"

			else:

				print "		disabled"


		print listOfNewPreferredCategories

		# now call the update of the new preferred categories
		joniConfig.api.updatePreferredNewsCategories(joniConfig.user,listOfNewPreferredCategories)

		joniConfig.areThereNewCategories = True

		# eventually call the superclass method
		super(SettingsPreferredCategories, self).handleInputReturn()

		# return self
		return self