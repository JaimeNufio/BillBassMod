from gtts import gTTS
from pygame import mixer # Load the required library

tts = gTTS(text="Hi Noralie", lang='en', slow = True)
tts.save("ttsText.mp3");

from pygame import mixer # Load the required library

mixer.init()
mixer.music.load('ttsText.mp3');
mixer.music.play()
