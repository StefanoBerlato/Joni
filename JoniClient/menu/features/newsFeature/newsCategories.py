# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import the needed classes:
# NavigableMenuOption 	: The mother class
# NewsTitles 			: The news title class  
# joniConfig 			: global config file
from menu.navigableMenuOption import NavigableMenuOption
from menu.features.newsFeature.newsTitles import NewsTitles
import config.joniConfig as joniConfig


# This is the news category class: it will be accessed in two ways:
#	- newsMode : thus from the news menu, and it will behaviour normally
#	- settingsMode : thus from the settings menu. This will affect its behaviour
class NewsCategories(NavigableMenuOption):
	__metaclass__ = ABCMeta

	# class constructor
	# ---- super class constructor options ----
	# @optionName the name of this option ("mainMenu", "settings", ...)
	# @optionNameAudioPath the path to the .mp3 file reproducing the name of this option
	# @previousMenuOption the reference to the object representing the previous menu option 
	# @followingMenuOptions the reference to the list of objects representing the following menu options 
	# @inputEventManager the global inputEventManager object
	# ---- class constructor ----
	# @settingsMode if this class is called from the settings menu or from the news menu, it should behaviour differently
	#	-	true : don't fetch the news. Instead, modify the action resulting from pressing the play button
	#	-	false: fetch the news. Don't modify the action resulting from pressing the play button
	# @enabled is this news category enabled? (option useful only for the settingsMode)

	def __init__(self, optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer, settingsMode, enabled):

		# to call the mother class init
		super(NewsCategories, self).__init__(optionName, optionNameAudioPath, previousMenuOption, followingMenuOptions, inputEventManager, audioPlayer)
		
		# set the variables with the given values
		self.settingsMode = settingsMode
		self.enabled = enabled


	# to string method
	def toString( self ):
		return ("News Category: " + self.optionName)


	# if the user pushes the play button
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputPlay( self ):

		# if we are in settings mode
		if (self.settingsMode):

			if (self.enabled):
				print "if enabled"
				self.enabled = False
				joniConfig.categoriesEnabled[self.optionName] = False
				self.reproduceOptionAudio(joniConfig.settingsPreferredCategoriesDisableAudioPath)
			else:
				print "if disabled"
				self.enabled = True
				joniConfig.categoriesEnabled[self.optionName] = True
				self.reproduceOptionAudio(joniConfig.settingsPreferredCategoriesEnableAudioPath)
			
			print joniConfig.categoriesEnabled

		# otherwise
		else:

			# just call the superclass method
			super(NewsCategories, self).handleInputPlay()

		return self


	# reproduce audio (if None, reproduce the first option audio if in newsMode. 
	# if in settingsMode, reproduce ENABLED or DISABLED)
	def reproduceOptionAudio( self, audio ):

		# if we are in settings mode
		if (self.settingsMode):

			if (self.enabled):
				audio = joniConfig.settingsPreferredCategoriesEnabledAudioPath
			else:
				audio = joniConfig.settingsPreferredCategoriesDisabledAudioPath
			
		# call the superclass method	
		super(NewsCategories, self).reproduceOptionAudio(audio)	


	# initialize the folowing options for this menu
	# note: Later on the construction of this list of options will be
	# optimized by integrating local data with new one from the server
	# @return self : this class, in order to be able to concatenate functions 
	def initializeFollowingOptions( self ):

		# if we are in settings mode
		if (self.settingsMode):

			# no following options
			self.setFollowingMenuOptions([])
			
		# otherwise, get the title of the news of this category
		else:

			# if we don't have already initialized the following options list OR there are new news
			if (not self.alreadyInitializedOptions or joniConfig.areThereNewNews) :

				# reproduce the downloadInProgressWithMusicAudioPath audio
				self.audioPlayer.reproduceAudio(joniConfig.downloadInProgressWithMusicAudioPath)

				# get the news titles
				listOfNewsTitlesJSON = joniConfig.api.getNewsTitlesByCategory(joniConfig.user,self.optionName)

				# temporary variable for the lists of titles of news
				listOfNewsTitles = []

				# for each defined category
				for i in range(len(listOfNewsTitlesJSON)):

					# compose the path to the title audio
					pathToNewsTitleAudio = joniConfig.newsBaseDirectoryAudioPath + "titles/" + listOfNewsTitlesJSON[i]["newsId"] + ".mp3"

					# create the related news title object
					newNews = NewsTitles(listOfNewsTitlesJSON[i]["newsId"], pathToNewsTitleAudio, self, None, self.inputEventManager, self.audioPlayer)
					
					# append it to the list
					listOfNewsTitles.append(newNews)

				# set (or reset) the following menu options
				self.setFollowingMenuOptions(listOfNewsTitles)

				self.alreadyInitializedOptions = True
				joniConfig.areThereNewNews = False

		# return self
		return self



	# if the user pushes the backward button, do nothing if we are in the settings mode
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputBackward( self ):

		# if we are in settings mode
		if (self.settingsMode):

			return self
			
		# otherwise, get the title of the news of this category
		else:

			return super(NewsCategories, self).handleInputBackward()



	# if the user pushes the backward button, do nothing if we are in the settings mode
	# @return self : this class, in order to be able to concatenate functions 
	def handleInputForward( self ):

		# if we are in settings mode
		if (self.settingsMode):

			return self
			
		# otherwise, get the title of the news of this category
		else:

			return super(NewsCategories, self).handleInputForward()
