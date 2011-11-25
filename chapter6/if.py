#!/usr/bin/python2
num = 1
guess = int(raw_input('guess a number:'))

if guess == num:
	print 'exactly!'
elif guess > num:
	print 'high'
else:
	print 'low'
print 'end'
