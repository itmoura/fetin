# -*- coding: utf-8 -*-
# coding: utf-8

# import pyttsx
# from gtts import gTTS
# from playsound import playsound
# pt_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"

class Voice:
    def fala(self, frase):
        print (frase)
        # engine = pyttsx.init('dummy')
        # def onWord(name, location, length):
        #     print 'word', name, location, length
        #     if location > 10:
        #         engine.stop()
        # print ("to aqui")
        # # engine.connect('started-word', onWord)
        # engine.setProperty('voice', pt_voice_id)
        # engine.say("Eu vou falar aqui tudo sobre a letra A!")
        # print ("to aqui depois")
        # engine.runAndWait()
        # print ("to aqui depois")
        # engine.setProperty('voice', pt_voice_id)
        # engine.say(frase)
        # engine.runAndWait()

# tts = gTTS(frase, lang='pt-br')
# #Salva o arquivo de audio
# tts.save('audio/aprender_com_floquinho.mp3')
# print("Reconhecendo a Frase")
# #Da play ao audio
# playsound("audio/aprender_com_floquinho.mp3")
# print ("terminei aqui")

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