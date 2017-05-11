from gtts import gTTS
import pygame, time, thread


pygame.mixer.init();

def speakWords(text): #From text, speak
	phrase=text;
	tts = gTTS(text=phrase, lang='en', slow = False)
	tts.save("ttsText.mp3");

	pygame.mixer.music.load("ttsText.mp3");
	pygame.mixer.music.play(0);

	while pygame.mixer.music.get_busy():
		pygame.time.delay(100);

def dummyTalk(): #do something while talking
	count = -1;
	while True:
		if pygame.mixer.music.get_busy():
			pygame.time.delay(150);
			print(count);	
			count*=-1;

#speakWords("Text speech working fine.");

# threads
#"""
thread.start_new_thread(speakWords,("Currently testing if threading works with this setup",))
thread.start_new_thread(dummyTalk,());

while 1:
	pass;
#"""
