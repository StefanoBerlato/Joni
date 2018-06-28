# import the needed classes:
# pygame	: module containing the mixer module to play the audio files
# sys 		: the operating system module
# subprocess: class to execute the bash script to decrease the volume
import pygame, sys
import subprocess

# This is the class that takes care of reproducing the audio files
# This also handle the volume (increment and decrement it by audioVolumeIncreaseDecreaseUnit)
# and the playback speed
class AudioPlayer:

	# class constructor
	# initialize the mixer module from pygame
	def __init__( self ):
		
		# retrieve the previously set volume
		self.audioVolume = 80

		# the value by which increase / decrease the volume
		self.audioVolumeIncreaseDecreaseUnit = 10 

		# the interval in which the audio volume should stay
		self.audioVolumeInterval = [0, 100]

		# initialize the audio module
		pygame.mixer.init()



	# to string method
	def toString( self ):
		return ("This is the only AudioPlayer in the world :D")



	# method reproducing audio. If another audio was being player when a new request arrives,
	# the previous one will fade out in half a second
	# @param audioFilePath : the path of the audio to reproduce
	# @return self : this class, in order to be able to concatenate functions 
	def reproduceAudio( self, audioFilePath ):

		if (not audioFilePath == None):

			# if another sound is being played
			if (pygame.mixer.get_busy()):

				# fadeout what were being played
				pygame.mixer.fadeout(500)

			#TODO testare il fadeout

			# load the file to be reproduce
			pygame.mixer.music.load(audioFilePath)

			# set the volume (When new music is loaded the volume is reset by the library)
			pygame.mixer.music.set_volume(self.audioVolume)

			# reproduce it
			pygame.mixer.music.play()

		# return self
		return self

		
	# increase the volume of the music module. This goes from 0.0 to 1.0
	# @return audioPlayer : this class, in order to be able to concatenate functions 
	def increaseAudioVolume ( self ): 

		# if the new volume is under the maximum
		if ( (self.audioVolume + self.audioVolumeIncreaseDecreaseUnit) <= self.audioVolumeInterval[1]):

			# increment the volume
			self.audioVolume = self.audioVolume + self.audioVolumeIncreaseDecreaseUnit

			bashCommand = "amixer set PCM -- " + str(self.audioVolume) +"%"
			process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output, error = process.communicate()

		# return self
		return self



	# decrease the volume of the music module. This goes from 0.0 to 1.0
	# @return audioPlayer : this class, in order to be able to concatenate functions 
	def decreaseAudioVolume ( self ): 

		# if the new volume is under the maximum
		if ( (self.audioVolume - self.audioVolumeIncreaseDecreaseUnit) >= self.audioVolumeInterval[0]):

			# increment the volume
			self.audioVolume = self.audioVolume - self.audioVolumeIncreaseDecreaseUnit

			bashCommand = "amixer set PCM -- " + str(self.audioVolume) +"%"
			process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output, error = process.communicate()

		# return self
		return self



