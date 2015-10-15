from copy import copy

def ncr_table(n):
	l = [1]
	for k in range(1, 1 + n // 2):
		l.append(l[k-1] * (n - k + 1)/k)
	c = copy(l)
	c.pop()
	c.reverse()
	if n % 2 == 1:
		l.append(l[-1])
	map(lambda x: l.append(x), c)
	l = map(lambda x: x % 10**9, l)
	return " ".join( map(str, l) )

cases = int(raw_input())
for i in range(cases):
	n = int(raw_input())
	print ncr_table(n)
