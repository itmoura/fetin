# -*- coding: utf-8 -*-
# coding: utf-8

import pyttsx3
import time
engine = pyttsx3.init("sapi5")
pt_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"

class Voice:
    def fala(self, frase):
        engine.setProperty('voice', pt_voice_id)
        engine.say(frase)
        engine.runAndWait()
        time.sleep(2)
        engine.disconnect()
        print ("terminei aqui")


# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)

# Use female English voice
# engine.setProperty('voice', en_voice_id)
# engine.say('Hello with my new voice')

# Use female Russian voice