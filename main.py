#!/usr/bin/env python3

from jarvis import Jarvis

def test():
  c = Jarvis()
  c.listenToMe()

test()

# while 1:
#   with sr.Microphone() as source:
#       audio = r.listen(source)
#   try:
#       order = Order(audio)
#       text = r.recognize_google(audio, language='fr-FR')
#       wiki_page = wiki.page(text)
#       if wiki_page.exists():
#         print(wiki_page.summary)
#       else:
#         print("Dites quelque chose")
#   except sr.UnknownValueError:
#       print("audio non compris")
#   except sr.RequestError as e:
#       print("Le service Google Speech API ne fonctionne plus" + format(e))