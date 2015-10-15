def palindrome_permutation(s):
	s = map(lambda x: ord(x) - ord('a'), list(s))
	h = [0] * 26
	for i in s:
		h[i] += 1
	odds = 0
	for i in h:
		if i % 2 == 1:
			odds += 1
	return odds <= 1

s = raw_input()
if palindrome_permutation(s):
	print "YES"
else:
	print "NO"
