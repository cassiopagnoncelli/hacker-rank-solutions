def palindrome_index(s):
	if len(s) <= 1:
		return -1
	mid = len(s) // 2
	last = len(s) - 1
	for i in range(mid):
		if s[i] != s[last - i]:
			r = s[:i:] + s[i+1::]
			if r == r[::-1]:
				return i
			else:
				return last - i
	return -1

n = int(raw_input())
for i in range(n):
	print palindrome_index(raw_input())
