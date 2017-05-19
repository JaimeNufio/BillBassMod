from gtts import gTTS
import pygame, time, thread 
import time, thread
#import RPi.GPIO as io;
#import MotorControl as motor

def speakWords(text): #From text, speak
	
	#TODO Implement the recording of new audio 
	#For now it'll suffice to just play prerecorded audio	

	#phrase=text;
	#tts = gTTS(text=phrase, lang='en', slow = False)
	#tts.save("ttsText.mp3");

	pygame.mixer.init();
	pygame.mixer.music.load("ttsText.mp3");
	pygame.mixer.music.play(0);

	while pygame.mixer.music.get_busy():
		pygame.time.delay(100);

	print("Stopped Talking");

#"""

#TODO Change this structure? 
#Maybe I should have a central func that accepts methods, rather than the opposite?

def dummyTalk(mSet): #do something while talking
	count = -1;
	while True:
		if pygame.mixer.music.get_busy():
			pygame.time.delay(150);
			motor.motorOff(mSet);
			print(count);	
			count*=-1;
			if count > 0:
				motor.motorOn(mSet);
			else:
				motor.motorOff(mSet);
	motor.Off(mSet);

#TODO Manange threads from FishPuppet.py
"""
def fishyTalk(mSet,text):
	thread.start_new_thread(speakWords,(text,))
	thread.start_new_thread(dummyTalk,(mSet,));
	while pygame.mixer.music.get_busy():
		pass;
	
	print("Finished Speaking");
"""


#speakWords("Text speech working fine.");

# threads
"""
thread.start_new_thread(speakWords,("Currently testing if threading works with this setup",))
thread.start_new_thread(dummyTalk,());

while 1:
	pass;
"""

speakWords("It finally worked!");
