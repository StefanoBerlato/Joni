# import the needed classes:
# Button	: Button class
# Switch 	: Switch class
# GPIO      : class for handling GPIO
# time      : class for handling timing
from objects.button import Button
from objects.switch import Switch
import RPi.GPIO as GPIO
import time


# This class is the one receiving all the user inputs first (through buttons and switches)
# It has associated an inputReceiver to redirect the inputs to
class InputEventManager:

	# class constructor. Needed Parameters area
	# @param buttons : the list of buttons 
	# @param switches : the list of switches
	# @param currentEventReceiver : the current event receiver. At the beginning, it should be the Option "mainMenu"  
	def __init__( self, buttons, switches, currentEventReceiver, audioPlayer, mainMenu ):

		# initialize the current event receiver
		self.currentEventReceiver = None

		self.audioPlayer = audioPlayer
		self.mainMenu = mainMenu

		# set the event receiver
		self.setEventReceiver (currentEventReceiver)
		
		# set the buttons and the switch list
		self.buttons = buttons
		self.switches = switches

		# the variable associated with the Lock switch
		self.buttonsLocked = False

		self.sleepTime = 0.75
		self.returnTimes = 0
		self.returnTimesToGoBackToMainMenu = 4 # 0.75*4 = 3 sec

	# to string method
	def toString( self ):
		return ("this is the only InputEventManager")



	# this method sets the event receiver 
	# @param newEventReceiver : the reference to the new event receiver object
	# @return currentEventReceiver : the new input event receiver
	def setEventReceiver( self, newEventReceiver ):

		# if it is not none
		if (not newEventReceiver == None):

			# debugging
			print ( "InputEventManager has set a new EventReceiver: " + newEventReceiver.toString() ) 

			# set the receiver
			self.currentEventReceiver = newEventReceiver

			# make it to reproduce its audio
			self.currentEventReceiver.reproduceOptionAudio("MenuIntro");

			# eventually, return
			return self.currentEventReceiver


	# get event receiver
	# @return currentEventReceiver : the current input event receiver
	def getEventReceiver( self ) : 
		return self.currentEventReceiver



	# this method start listening for inputs
	def registerInputs( self ):
	
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(6,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		while (True) :

			if (  GPIO.input(21) == False  ):
		 		print ("Pin  21 ok is pressed")
		 		self.currentEventReceiver.handleInputPlay()
		 		time.sleep(self.sleepTime)
		 		
			elif (GPIO.input(6) == False):
				print ("Pin  6 indietro is pressed")
				self.returnTimes = self.returnTimes + 1
				time.sleep(self.sleepTime)
		 		
			elif (GPIO.input(16) == False):
				print ("Pin  16 forward is pressed")
				self.currentEventReceiver.handleInputForward()
				time.sleep(self.sleepTime)
		 		
			elif (GPIO.input(19) == False):
				print ("Pin  19 backwarwd is pressed")
				self.currentEventReceiver.handleInputBackward()
				time.sleep(self.sleepTime)

			elif (GPIO.input(17) == False):
				print ("Pin  17 volume up is pressed")
				self.audioPlayer.increaseAudioVolume();
				time.sleep(self.sleepTime)

			elif (GPIO.input(12) == False):
				print ("Pin  12 volume down is pressed")
				self.audioPlayer.decreaseAudioVolume();
				time.sleep(self.sleepTime)


			# if the return button is NOT pressed
			if (GPIO.input(6) == True):
				if (self.returnTimes > 0 and self.returnTimes < self.returnTimesToGoBackToMainMenu):
					self.currentEventReceiver.handleInputReturn()
				elif (self.returnTimes >= self.returnTimesToGoBackToMainMenu):
					# set the event receiver to be the previous Option object
					self.setEventReceiver(self.mainMenu)

				self.returnTimes = 0


	# what happens when the user pushes the lock button?
	def receiveLockSwitchEvent( self ) : 

		# set the block to the buttons
		self.buttonsLocked = not self.buttonsLocked


	# what happens when the user pushes the power button?
	def receivePowerSwitchEvent( self ) : 

		print (self.toString() + ": spegnimento...")
		# ----- to be changed in the raspberry -----