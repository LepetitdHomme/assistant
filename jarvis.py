#!/usr/bin/env python3

import speech_recognition as sr
from order import Order
from wiki import WikiSearch
from texttospeech import ToSpeech

class Jarvis:
  def __init__(self):
    self.r = sr.Recognizer()

  def listenToMe(self):
    while True:
      with sr.Microphone() as source:
        audio = self.r.listen(source)
      try:
        text = self.r.recognize_google(audio, language='fr-FR')
        print(text)
        commands = Order(text).commands
        for x in commands:
          print(x)
        if commands[0] == 'recherche':
          if len(commands) < 2:
            print('no word to search')
          else:
            wikiSearch = WikiSearch(commands[1])
            print(wikiSearch.summary())
            voice = ToSpeech(wikiSearch.summary())
            voice.speak()

      except sr.UnknownValueError:
        print("audio non compris")
      except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))
