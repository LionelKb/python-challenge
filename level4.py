#!/usr/bin/env python2

import urllib

def next_nothing(nothing):
  url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
  f = urllib.urlopen(url)
  nothing = f.read()
  nothing = nothing.split(" ")[-1] 
  return nothing

nothing = "12345"
for _ in range(400):
  nothing = next_nothing(nothing)
  print nothing
