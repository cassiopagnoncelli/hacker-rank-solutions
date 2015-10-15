n = int(raw_input())
scores = {}
for i in range(n):
	name = raw_input()
	score = float(raw_input())
	if score in scores:
		scores[score].append(name)
	else:
		scores[score] = [ name ]

keys = sorted(scores.keys())
if len(keys) == 1:
	second = keys[0]
else:
	second = keys[1]

vals = sorted(scores[second])
for v in vals:
	print v
