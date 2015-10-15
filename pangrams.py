def pangram(s):
	p = map(lambda x: ord(x) - ord('a'), list(s.lower()))
	h = [0] * 26
	for c in p:
		if c >= 0 and c <= 25:
			h[c] += 1
	for c in h:
		if c == 0:
			return False
	return True

if pangram(raw_input()):
	print "pangram"
else:
	print "not pangram"
