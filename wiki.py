#!/usr/bin/env python3

import wikipediaapi
wiki = wikipediaapi.Wikipedia('fr')

class WikiSearch:
  def __init__(self, text):
    self.text = text

  def summary(self):
    wiki_page = wiki.page(self.text)
    if wiki_page.exists():
      return wiki_page.summary
    else:
      return 'non trouve'
