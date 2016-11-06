#!/usr/bin/env python

import urllib
import re

def next_nothing(nothing):
  url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
  url += nothing
  f = urllib.urlopen(url)
  nothing = f.read()
  return nothing

nothing = "12345"
while True:
  nothing = next_nothing(nothing)
  print nothing
  match =  re.match(r".*and the next nothing is (\d+)",nothing)
  if match == None:
    if "going" not in nothing:
      print nothing
      break
  else: 
    nothing = match.group(1)
