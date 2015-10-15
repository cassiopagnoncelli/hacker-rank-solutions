def changes(s):
	s = map(lambda x: ord(x) - ord('a'), list(s))
	q = len(s) // 2
	last = len(s) - 1
	d = 0
	for i in range(q):
		d += abs( s[i] - s[last-i] )
	return d

n = int(raw_input())
for i in range(n):
	print changes(raw_input())
