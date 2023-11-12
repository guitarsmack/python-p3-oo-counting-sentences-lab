#!/usr/bin/env python3

class MyString:

  def __init__(self,value = ''):
    if isinstance(value,str) and len(value) != 0:
      self.value = value
    else:
      self.value = ''
      print("The value must be a string.")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def is_sentence(self):
    return self.value.endswith(".")
  
  def count_sentences(self):
    if len(self.value) == 0:
      return 0
    else:
      return len(self.value.replace("!",".").replace("?",".").split(". "))


