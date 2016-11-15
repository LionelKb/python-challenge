#!/usr/bin/env python

import pickle

message = pickle.load(open("mess-level5.p","r"))

for line in message:
	str_line = ""
	for values in line:
		str_line += values[0] * values[1] 
	print str_line