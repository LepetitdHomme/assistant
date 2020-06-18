#!/usr/bin/env python3

class Order:
  def __init__(self, text):
    self.text = text
    self.commands = text.split()
