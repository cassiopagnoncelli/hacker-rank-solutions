def make_it_anagram(A, B):
	A = map(lambda x: ord(x) - ord('a'), list(A))
	B = map(lambda x: ord(x) - ord('a'), list(B))
	hA = [0] * 26
	hB = [0] * 26
	for i in A:
		hA[i] += 1
	for i in B:
		hB[i] += 1
	d = 0
	for i in range(26):
		d += abs(hA[i] - hB[i])
	return d

A = raw_input()
B = raw_input()
print make_it_anagram(A, B)
