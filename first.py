def function(base, exp):
	result = base
	for x in xrange(1,exp):
		result = result * base
	return result

print function(2, 38)