def uniques(s):
	chars = map(lambda x: ord(x) - ord('a'), list(s))
	h = [0] * 26
	for c in chars:
		if h[c] == 0:
			h[c] += 1
	return h

def gem_stones(strings):
	letters = [0] * 26
	for s in strings:
		h = uniques(s)
		for i in range(len(h)):
			if h[i] == 1:
				letters[i] += 1
	gem_elements = 0
	for i in range(len(letters)):
		if letters[i] == len(strings):
			gem_elements += 1
	return gem_elements

n = int(raw_input())
strings = []
for i in range(n):
	strings.append(list(raw_input()))

print gem_stones(strings)
