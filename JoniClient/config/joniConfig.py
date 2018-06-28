	# This is the Joni configuration file, where all settings are stored
# (buttons/switches, static file paths, ...)


# ----- Start of Modifiable parameters -----

# button properties
buttonNames = ["play", "return", "forward", "backward", "volumeUp", "volumeDowm"]
buttonPinNumbers = [0, 1, 2, 3, 4, 5]

# switch properties
switchNames = ["power", "lock"]
switchPinNumbers = [6, 7]

# list of audio paths
menuBaseDirectoryAudioPath = "./media/audio/menu/"
welcomeAudioPath = "./media/audio/menu/MainMenu.mp3"
newsMenuAudioPath = "./media/audio/menu/news.mp3"
settingsMenuAudioPath = "./media/audio/menu/settings.mp3"
noMenuOptionAvailableAudioPath = "./media/audio/menu/noNewsAvailable.mp3"
settingsPreferredCategoriesAudioPath = "./media/audio/menu/settingsSetYourPreferredCategories.mp3"
settingsPreferredCategoriesEnableAudioPath = "./media/audio/menu/settingsEnableCategory.mp3"
settingsPreferredCategoriesDisableAudioPath = "./media/audio/menu/settingsDisableCategory.mp3"
settingsPreferredCategoriesEnabledAudioPath = "./media/audio/menu/settingsEnabledCategory.mp3"
settingsPreferredCategoriesDisabledAudioPath = "./media/audio/menu/settingsDisabledCategory.mp3"
downloadInProgressAudioPath = "./media/audio/menu/waiting.mp3"
downloadInProgressWithMusicAudioPath = "./media/audio/menu/waitingMusic.mp3"
newsBaseDirectoryAudioPath = "./media/audio/news/"

# list of category audio paths
categoriesAudioPaths = ["./media/audio/categories/business.mp3", 
						"./media/audio/categories/entertainment.mp3", 
						"./media/audio/categories/general.mp3",
						"./media/audio/categories/health.mp3",
						"./media/audio/categories/science.mp3",
						"./media/audio/categories/sports.mp3",
						"./media/audio/categories/technology.mp3"]
categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
categoriesEnabled = {"business": False, "entertainment": False, "general": False, "health": False, "science": False, "sports": False, "technology":False}


# ----- End of modifiable parameters -----

# this will be the variable containing the reference to the User and NewsAPIDAOImpl objects
user = None
api = None

# if there are new categories, we have to re-initialize the newsMenu menu
areThereNewCategories = True

# if there are new categories, we have to re-initialize the newsCategories menus
areThereNewNews = True