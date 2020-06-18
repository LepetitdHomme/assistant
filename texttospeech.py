#!/usr/bin/env python3

from gtts import gTTS
import os

class ToSpeech:
  def __init__(self, text):
    self.text = text
    self.language = 'fr'

  def speak(self):
    obj = gTTS(text=self.text, lang=self.language, slow=False)
    obj.save('text.mp3')
    os.system('mpg321 text.mp3')