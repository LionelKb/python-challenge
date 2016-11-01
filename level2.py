#!/usr/bin/env python2
from collections import Counter

counter = Counter()
with open("mess.txt",'r') as f:
  mess = f.readlines()

mess = "".join(mess) 
mess = mess.replace("\n","")
for c in map(None,mess):
  counter[c] += 1

# sort counter
counter_rare_chars = counter.most_common()[-8:]
rare_chars = {}
for c in counter_rare_chars:
  rare_chars[mess.index(c[0])] = c[0]

rare_chars = sorted(rare_chars.items())
result = ""
for k,v in rare_chars:
 result += v

print result


