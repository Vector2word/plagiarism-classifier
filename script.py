# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:27:02 2021

@author: My Lenovo
"""

import nltk
# Levenshtein distance:
from nltk.metrics import edit_distance

# an arbitrary plagiarism classifier:
def is_plagiarized(text1, text2):
  n = 7
  if edit_distance(text1.lower(), text2.lower()) > ((len(text1) + len(text2)) / n):
    return False
  return True

doc1 = "i do not now"
doc2 = "i do not now maybe"

print(is_plagiarized(doc1, doc2))