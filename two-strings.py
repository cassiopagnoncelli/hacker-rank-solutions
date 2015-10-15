def two_strings(S, T):
	hT = [0] * 26
	for i in T:
		hT[i] = 1
	for c in S:
		if hT[c] == 1:
			return True
	return False

n = int(raw_input())
for i in range(n):
	s = map(lambda x: ord(x) - ord('a'), list(raw_input()))
	t = map(lambda x: ord(x) - ord('a'), list(raw_input()))
	if two_strings(s, t):
		print "YES"
	else:
		print "NO"
