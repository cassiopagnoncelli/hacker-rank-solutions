def anagram(s):
	if len(s) % 2 == 1:
		return -1
	mid = len(s) // 2
	A = map(lambda x: ord(x) - ord('a'), list(sorted(s[:mid:])))
	B = map(lambda x: ord(x) - ord('a'), list(sorted(s[mid::])))
	d = 0
	for i in range(len(A)):
		if A[i] != B[i]:
			d += 1
	return d

n = int(raw_input())
for i in range(n):
	print anagram(raw_input())
