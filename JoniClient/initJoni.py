# import the needed classes:
# InputEventManager 	: The class that handles the user events, button and switches
# MainMenu 				: To istantiate the mainMenu class
# AudioPlayer 			: The class that handles the audio streams
# Switch 				: Switch class, to initialize them
# Button 				: Button class, to initialize them
# User 					: User class, to initialize it
# NewsAPIDAOImpl        : class for API requests, to initialize it
# joniConfig 			: General file containing configuration values
# threading 			: To do a request for new news each 15 minutes
from util.inputEventManager import InputEventManager
from menu.mainMenu import MainMenu
from util.audioPlayer import AudioPlayer
from objects.switch import Switch
from objects.button import Button
from objects.user import User
from newsAPI.newsAPIDAOImpl import NewsAPIDAOImpl
import config.joniConfig as joniConfig
import threading

# getting the configuration values for buttons and switches
buttonNames = joniConfig.buttonNames
switchNames = joniConfig.switchNames
buttonPinNumbers = joniConfig.buttonPinNumbers
switchPinNumbers = joniConfig.switchPinNumbers

# the variable that will store the just created buttons
buttons = []
# the variable that will store the just created switches
switches = []

# for each defined button
for i in range(len(buttonNames)):
	# create the buttons
	buttons.append(Button(buttonNames[i], buttonPinNumbers[i]))

# for each defined switch
for i in range(len(switchNames)):
	# create the switches
	switches.append(Switch(switchNames[i], switchPinNumbers[i]))

# create the class that will handle the audio event
audioPlayer = AudioPlayer()



# menu tree
#
#					| Main Menu |
#			  	 |  News  | Settings |	
#		list of categories| set your preferred categories
#		list of titles	  |
#		list of news	  |

#create the current event receiver, thus the Main Menu
mainMenu = MainMenu("MainMenu", joniConfig.welcomeAudioPath, None, None, None, audioPlayer);

# create the class that will manage the input button events
inputManager = InputEventManager(buttons, switches, None, audioPlayer, mainMenu)

mainMenu.inputEventManager = inputManager

# make him to initialize his own subMenu
mainMenu.initializeFollowingOptions();

# set the first receiver (the main menu)
inputManager.setEventReceiver(mainMenu)

# initialize the user and the api classes
joniConfig.user = User(1)
joniConfig.api = NewsAPIDAOImpl() 



# to update news each 15 minutes
def updateNews():
  threading.Timer(900.0, updateNews).start()
  print "areThereNewNews = true"
  joniConfig.areThereNewNews = True 
updateNews()


# last line of code!
inputManager.registerInputs();