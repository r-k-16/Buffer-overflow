#!/usr/bin/python3

import string, sys

num = '0123456789'
la = string.ascii_lowercase
ua = string.ascii_uppercase

val = ''
i,j,k = 0,0,0

def pattern_create(counter):
	global val,i,j,k

	while counter > len(val):
		val = val + ua[i]	#ABC
		while counter > len(val) and ((len(val) % 3) == 1 or len(val) < 3):
			val = val + la[j]	#abc
			while counter > len(val):
				val = val + num[k]	#012
				k += 1
				if (j == len(la) - 1) and k == len(num):
					i += 1
					j = 0
					k = 0
				elif k == len(num):
					j += 1
					k = 0
				break
	print(val)

def find_offset(offset):
	# Hex to ASCII e.g: 41307241(offset value) -> Ar0A
	# http://defindit.com/ascii.html
	# 41307241 -> \x41 - A, \x72 - r, \x30 - 0 , \x41 - A
	global val,i,j,k
	x = 0
	off_val = ''
	list_value = ''

	for offset_val in offset:
		list_value = list_value + offset_val
		if len(list_value) == 2:
			offset_string = chr(int(list_value,16))
			off_val = off_val + offset_string
			list_value = ''
	off_val = off_val[::-1]

	while off_val not in val:
		val = val + ua[i]
		while off_val not in val and ((len(val) % 3) == 1 or len(val) < 3):
			val = val + la[j]
			while off_val not in val:
				val = val + num[k]
				k += 1
				if (j == len(la) - 1) and k == len(num):
					i += 1
					j = 0
					k = 0
				elif k == len(num):
					j += 1
					k = 0
				break
	print(len(val) - 4)

def syntax_check():
	print("Invalid argument")
	print("Create Pattern:	" + sys.argv[0] + " -p 896")
	print("Find Offset:	" + sys.argv[0] + " -f 41307241")

try:
	if sys.argv[1] == '-p':
		pattern_create(int(sys.argv[2]))
	elif sys.argv[1] == '-f':
		find_offset(sys.argv[2])
	else:
		syntax_check()
		
except:
	syntax_check()
