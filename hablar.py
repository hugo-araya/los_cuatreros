from gtts import gTTS
import os
from playsound import playsound

texto = input("Ingrese un texto: ")
tts = gTTS(text = texto, lang='es')
tts.save('tecsify.mp3')
playsound('tecsify.mp3')

