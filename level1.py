#!/usr/bin/env python2


# Level 1

# K -> M
# O -> Q
# E -> G

def translation(str):
  result = ""
  alphabet =  map(chr, range(97, 123))
  translation = alphabet[2:]
  translation.append('a')
  translation.append('b')

  for c in str:
    if c in alphabet:
      c = translation[alphabet.index(c)]
    result += c
  print result


def translation_refactored(str):
  from string import maketrans

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  mapped = "cdefghijklmnopqrstuvwxyzab"
  translation = maketrans(alphabet,mapped)
  print str.translate(translation)


original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url = "http://www.pythonchallenge.com/pc/def/map.html"
translation_refactored(url)

