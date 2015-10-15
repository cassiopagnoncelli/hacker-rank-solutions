def dels(s):
	l = list(s)
	c = 0
	for i in range(len(l)-1):
		if l[i+1] == l[i]:
			c += 1
	return c

n = int(raw_input())
for i in range(n):
	print dels(raw_input())
