while True:
	s = raw_input('enter something: ')
	if s == 'q':
		break
	if len(s) < 6:
		continue
	print 'too long'
print 'done'
