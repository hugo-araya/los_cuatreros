from gtts import gTTS
import os
from playsound import playsound

texto = input("Ingrese un texto: ")
tts = gTTS(text = texto, lang='pt')
tts.save('habla.mp3')
playsound('habla.mp3')

