def pass_day(plants):
	stack = [plants[0]]
	last = plants[0]
	for i in range(1, len(plants)):
		x = plants[i]
		if x <= last:
			stack.append(x)
			last = x
		else:
			last = x
	return stack

ignore = int(raw_input())
plants = map(int, raw_input().strip().split())

l = len(plants)
count = 1
while True:
	r = pass_day(plants)
	if len(r) == l:
		print count
		break
	else:
		count += 1
		l = len(r)
