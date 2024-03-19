#!/usr/bin/python3

import string

num = '0123456789'
la = string.ascii_lowercase
ua = string.ascii_uppercase

val = ''
i,j,k = 0,0,0

def pattern_create():
	counter = int(input("Enter the pattern length: "))
	if counter > 20280:
		print("Pattern length exceeds the limit, Try Again...")
		exit()
	global val,i,j,k

	while counter > len(val):
		val = val + ua[i]
		while counter > len(val) and ((len(val) % 3) == 1 or len(val) < 3):
			val = val + la[j]
			while counter > len(val):
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
	print(val)

def find_offset():
	# Hex to ASCII e.g: 41307241(offset value) -> Ar0A
	# http://defindit.com/ascii.html
	# 41307241 -> \x41 - A, \x72 - r, \x30 - 0 , \x41 - A
	global val,i,j,k
	x = 0
	off_val = ''
	list_value = ''
	offset = input("Enter the offset value: ")

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

print("1. Create pattern")
print("2. Find Offset")
choice = int(input("Enter you choice (1 or 2): "))

if choice == 1:
	pattern_create()
elif choice == 2:
	find_offset()
else:
	print("Invalid choice...")
