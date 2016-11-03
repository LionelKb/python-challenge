#!/usr/bin/env python2
import re

with open("mess-level3.txt","r") as f:
  mess = f.read()
regex = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"
matches = re.findall(regex,mess)
print "".join(matches)
