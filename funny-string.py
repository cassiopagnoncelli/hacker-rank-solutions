def diff_list(s):
	l = map(lambda x: ord(x), list(s))
	r = []
	for i in range(len(l)-1):
		r.append(abs(l[i+1] - l[i]))
	return r

def test(s):
	A = diff_list(s)
	B = diff_list(s[::-1])
	for i in range(len(A)):
		if A[i] != B[i]:
			return False
	return True

n = int(raw_input())
for i in range(n):
	if test(raw_input()):
		print "Funny"
	else:
		print "Not Funny"
