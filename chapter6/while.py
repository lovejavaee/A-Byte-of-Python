#/usr/bin/python2
num = 5
i = True
while i:
	guess = int(raw_input('input:'))
	if guess == num:
		i = False
		print 'right,quit'
		print 'num is: ', num
	elif guess > num:
		print 'too high'
	else:
		print 'too low'
print 'done'
